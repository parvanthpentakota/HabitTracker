import json

class Habit:
    def __init__(self, name, progress=0, streak=0, longest_streak=0):
        self.name = name
        self.progress = progress
        self.streak = streak
        self.longest_streak = longest_streak

    def mark_done(self):
        self.progress += 1
        self.streak += 1

        if self.streak > self.longest_streak:
            self.longest_streak = self.streak

    def reset_streak(self):
        self.streak = 0

    def to_dict(self):
        return {
            "name": self.name,
            "progress": self.progress,
            "streak": self.streak,
            "longest_streak": self.longest_streak
        }

    @staticmethod
    def from_dict(data):
        return Habit(
            data["name"],
            data["progress"],
            data.get("streak", 0),
            data.get("longest_streak", 0)
        )

    def __str__(self):
        return (
            f"{self.name} → Progress: {self.progress} | "
            f"Current Streak: {self.streak} | "
            f"Longest Streak: {self.longest_streak}"
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
    habits.append(Habit(name))

    print("Habit added successfully!")


def mark_habit_done(habits):
    display_habits(habits)

    try:
        index = int(input("Select habit number: ")) - 1

        habits[index].mark_done()

        print("Habit marked as done!")

    except:
        print("Invalid choice!")


# 🔥 NEW FEATURE
def reset_habit_streak(habits):
    display_habits(habits)

    try:
        index = int(input("Select habit number to reset streak: ")) - 1

        habits[index].reset_streak()

        print("Current streak reset!")

    except:
        print("Invalid choice!")


def show_streak_summary(habits):
    if not habits:
        print("No habits available.")
        return

    print("\n=== Streak Summary ===")

    for habit in habits:
        print(
            f"{habit.name} → Current: {habit.streak}, "
            f"Longest: {habit.longest_streak}"
        )


def main():
    habits = load_habits()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Reset Streak")        # NEW
        print("5. Streak Summary")      # NEW
        print("6. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_habit(habits)

        elif choice == "2":
            mark_habit_done(habits)

        elif choice == "3":
            display_habits(habits)

        elif choice == "4":
            reset_habit_streak(habits)

        elif choice == "5":
            show_streak_summary(habits)

        elif choice == "6":
            save_habits(habits)

            print("Habits saved. Exiting...")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()