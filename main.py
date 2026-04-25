import json

class Habit:
    def __init__(self, name, progress=0):
        self.name = name
        self.progress = progress

    def mark_done(self):
        self.progress += 1

    def to_dict(self):
        return {"name": self.name, "progress": self.progress}

    @staticmethod
    def from_dict(data):
        return Habit(data["name"], data["progress"])

    def __str__(self):
        return f"{self.name} → Days Completed: {self.progress}"


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
        print("Habit marked as done!")
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


# 🔥 NEW FEATURE
def edit_habit(habits):
    display_habits(habits)
    try:
        index = int(input("Select habit to edit: ")) - 1
        new_name = input("Enter new name: ")
        habits[index].name = new_name
        print("Habit updated!")
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
        print("5. Edit Habit")   # NEW
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
            edit_habit(habits)
        elif choice == "6":
            save_habits(habits)
            print("Habits saved. Exiting...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()





