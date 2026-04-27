import json

class Habit:
    def __init__(self, name, progress=0, streak=0):
        self.name = name
        self.progress = progress
        self.streak = streak

    def mark_done(self):
        self.progress += 1
        self.streak += 1  # increase streak

    def reset_streak(self):
        self.streak = 0

    def to_dict(self):
        return {
            "name": self.name,
            "progress": self.progress,
            "streak": self.streak
        }

    @staticmethod
    def from_dict(data):
        return Habit(data["name"], data["progress"], data.get("streak", 0))

    def __str__(self):
        return f"{self.name} → Done: {self.progress} | Streak: {self.streak}"


def save_habits(habits):
    with open("habits.json", "w") as f:
        json.dump([h.to_dict() for h in habits], f)


def load_habits():
    try:
        with open("habits.json", "r") as f:
            data = json.load(f)
            return [Habit.from_dict(d) for d in data]
    except:
        return []


def display_habits(habits):
    if not habits:
        print("No habits found.")
        return

    print("\nYour Habits:")
    for i, habit in enumerate(habits):
        print(f"{i + 1}. {habit}")


def add_habit(habits):
    name = input("Enter habit name: ")
    habits.append(Habit(name))
    print("Habit added!")


def mark_habit_done(habits):
    display_habits(habits)
    try:
        index = int(input("Select habit number: ")) - 1
        habits[index].mark_done()
        print("Habit marked as done! 🔥 Streak increased!")
    except:
        print("Invalid choice!")


def reset_streak(habits):
    display_habits(habits)
    try:
        index = int(input("Select habit to reset streak: ")) - 1
        habits[index].reset_streak()
        print("Streak reset!")
    except:
        print("Invalid choice!")


def delete_habit(habits):
    display_habits(habits)
    try:
        index = int(input("Select habit to delete: ")) - 1
        removed = habits.pop(index)
        print(f"Deleted habit: {removed.name}")
    except:
        print("Invalid choice!")


def main():
    habits = load_habits()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Delete Habit")
        print("5. Reset Streak")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_habit_done(habits)
        elif choice == "3":
            display_habits(habits)
        elif choice == "4":
            delete_habit(habits)
        elif choice == "5":
            reset_streak(habits)
        elif choice == "6":
            save_habits(habits)
            print("Habits saved. Exiting...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()





