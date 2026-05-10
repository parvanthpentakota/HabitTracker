import json

class Habit:
    def __init__(self, name, progress=0, goal=7):
        self.name = name
        self.progress = progress
        self.goal = goal

    def mark_done(self):
        self.progress += 1

    def progress_percentage(self):
        return min((self.progress / self.goal) * 100, 100)

    def goal_completed(self):
        return self.progress >= self.goal

    def to_dict(self):
        return {
            "name": self.name,
            "progress": self.progress,
            "goal": self.goal
        }

    @staticmethod
    def from_dict(data):
        return Habit(
            data["name"],
            data["progress"],
            data.get("goal", 7)
        )

    def __str__(self):
        status = "✅ Goal Achieved" if self.goal_completed() else "⏳ In Progress"

        return (
            f"{self.name} → {self.progress}/{self.goal} "
            f"({self.progress_percentage():.1f}%) | {status}"
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

    print("\n=== Your Habits ===")

    for i, habit in enumerate(habits):
        print(f"{i + 1}. {habit}")


def add_habit(habits):
    name = input("Enter habit name: ")

    try:
        goal = int(input("Enter target goal count: "))
    except:
        goal = 7

    habits.append(Habit(name, goal=goal))

    print("Habit added successfully!")


def mark_habit_done(habits):
    display_habits(habits)

    try:
        index = int(input("Select habit number: ")) - 1
        habits[index].mark_done()

        print("Habit marked as completed for today!")

    except:
        print("Invalid choice!")


# 🔥 NEW FEATURE
def show_goal_summary(habits):
    if not habits:
        print("No habits available.")
        return

    print("\n=== Goal Summary ===")

    completed_goals = 0

    for habit in habits:
        print(habit)

        if habit.goal_completed():
            completed_goals += 1

    print(f"\nGoals Achieved: {completed_goals}/{len(habits)}")


def main():
    habits = load_habits()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Goal Summary")   # NEW
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_habit(habits)

        elif choice == "2":
            mark_habit_done(habits)

        elif choice == "3":
            display_habits(habits)

        elif choice == "4":
            show_goal_summary(habits)

        elif choice == "5":
            save_habits(habits)
            print("Habits saved. Exiting...")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()