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


# 🔥 NEW FEATURE
def search_habit(habits):
    keyword = input("Enter habit name to search: ").lower()

    found = False
    for habit in habits:
        if keyword in habit.name.lower():
            print("Found:", habit)
            found = True

    if not found:
        print("No matching habit found.")


def main():
    habits = load_habits()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Search Habit")   # NEW
        print("5. Save & Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_habit_done(habits)
        elif choice == "3":
            display_habits(habits)
        elif choice == "4":
            search_habit(habits)
        elif choice == "5":
            save_habits(habits)
            print("Saved. Exiting...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()