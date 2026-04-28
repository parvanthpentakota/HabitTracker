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


# 🔥 NEW FEATURE
def show_summary(habits):
    total = len(habits)
    completed = sum(1 for h in habits if h.progress > 0)

    if total == 0:
        print("No habits to summarize.")
        return

    percentage = (completed / total) * 100
    print(f"\nSummary:")
    print(f"Total Habits: {total}")
    print(f"Completed Habits: {completed}")
    print(f"Completion: {percentage:.2f}%")



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


def main():
    habits = load_habits()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Show Summary")  # NEW
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_habit_done(habits)
        elif choice == "3":
            display_habits(habits)
        elif choice == "4":
            show_summary(habits)
        elif choice == "5":
            save_habits(habits)
            print("Habits saved. Exiting...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()