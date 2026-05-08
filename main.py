import json
from datetime import datetime

class Habit:
    def __init__(self, name, progress=0, history=None):
        self.name = name
        self.progress = progress
        self.history = history if history else []

    def mark_done(self):
        self.progress += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(timestamp)

    def to_dict(self):
        return {
            "name": self.name,
            "progress": self.progress,
            "history": self.history
        }

    @staticmethod
    def from_dict(data):
        return Habit(
            data["name"],
            data["progress"],
            data.get("history", [])
        )

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


# 🔥 NEW FEATURE
def show_history(habits):
    display_habits(habits)

    try:
        index = int(input("Select habit number to view history: ")) - 1
        habit = habits[index]

        print(f"\nCompletion History for {habit.name}:")

        if not habit.history:
            print("No completion history found.")
            return

        for entry in habit.history:
            print(entry)

    except:
        print("Invalid choice!")


def main():
    habits = load_habits()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. View Completion History")  # NEW
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_habit_done(habits)
        elif choice == "3":
            display_habits(habits)
        elif choice == "4":
            show_history(habits)
        elif choice == "5":
            save_habits(habits)
            print("Saved. Exiting...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()

