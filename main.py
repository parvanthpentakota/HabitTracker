import json
from datetime import datetime

class Habit:
    def __init__(self, name, progress=0, weekly_count=0):
        self.name = name
        self.progress = progress
        self.weekly_count = weekly_count

    def mark_done(self):
        self.progress += 1
        self.weekly_count += 1

    def reset_weekly_count(self):
        self.weekly_count = 0

    def to_dict(self):
        return {
            "name": self.name,
            "progress": self.progress,
            "weekly_count": self.weekly_count
        }

    @staticmethod
    def from_dict(data):
        return Habit(
            data["name"],
            data["progress"],
            data.get("weekly_count", 0)
        )

    def __str__(self):
        return (
            f"{self.name} → Total: {self.progress} | "
            f"Weekly: {self.weekly_count}"
        )


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
def show_weekly_report(habits):
    if not habits:
        print("No habits available.")
        return

    print("\n=== Weekly Habit Report ===")

    total_weekly = 0

    for habit in habits:
        print(f"{habit.name}: {habit.weekly_count} completions this week")
        total_weekly += habit.weekly_count

    print(f"\nTotal Weekly Completions: {total_weekly}")


def reset_weekly_report(habits):
    for habit in habits:
        habit.reset_weekly_count()

    print("Weekly report reset successfully!")


def main():
    habits = load_habits()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Weekly Report")      # NEW
        print("5. Reset Weekly Report")
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_habit_done(habits)
        elif choice == "3":
            display_habits(habits)
        elif choice == "4":
            show_weekly_report(habits)
        elif choice == "5":
            reset_weekly_report(habits)
        elif choice == "6":
            save_habits(habits)
            print("Saved. Exiting...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
