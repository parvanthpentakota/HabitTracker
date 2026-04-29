import json

class Habit:
    def __init__(self, name, progress=0, done_today=False):
        self.name = name
        self.progress = progress
        self.done_today = done_today

    def mark_done(self):
        if not self.done_today:
            self.progress += 1
            self.done_today = True

    def reset_today(self):
        self.done_today = False

    def to_dict(self):
        return {
            "name": self.name,
            "progress": self.progress,
            "done_today": self.done_today
        }

    @staticmethod
    def from_dict(data):
        return Habit(
            data["name"],
            data["progress"],
            data.get("done_today", False)
        )

    def __str__(self):
        status = "✅ Done Today" if self.done_today else "❌ Not Done"
        return f"{self.name} → Total: {self.progress} | {status}"


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
        print("Marked as done for today!")
    except:
        print("Invalid choice!")


# 🔥 NEW FEATURE
def reset_daily_status(habits):
    for h in habits:
        h.reset_today()
    print("Daily status reset for all habits!")


def main():
    habits = load_habits()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done Today")
        print("3. View Habits")
        print("4. Reset Daily Status")  # NEW
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_habit_done(habits)
        elif choice == "3":
            display_habits(habits)
        elif choice == "4":
            reset_daily_status(habits)
        elif choice == "5":
            save_habits(habits)
            print("Saved. Exiting...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()