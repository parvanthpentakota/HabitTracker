class Habit:
    def __init__(self, name):
        self.name = name
        self.progress = 0

    def mark_done(self):
        self.progress += 1

    def __str__(self):
        return f"{self.name} → Days Completed: {self.progress}"


def display_habits(habits):
    if not habits:
        print("No habits found.")
        return

    print("\nYour Habits:")
    for i, habit in enumerate(habits):
        print(f"{i + 1}. {habit}")


def add_habit(habits):
    name = input("Enter habit name: ").strip()
    if name:
        habits.append(Habit(name))
        print("Habit added successfully!")
    else:
        print("Habit name cannot be empty!")


def mark_habit_done(habits):
    if not habits:
        print("No habits to update.")
        return

    display_habits(habits)
    try:
        index = int(input("Select habit number: ")) - 1
        if 0 <= index < len(habits):
            habits[index].mark_done()
            print("Habit marked as done!")
        else:
            print("Invalid index!")
    except ValueError:
        print("Please enter a valid number!")


def main():
    habits = []

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_habit(habits)
        elif choice == "2":
            mark_habit_done(habits)
        elif choice == "3":
            display_habits(habits)
        elif choice == "4":
            print("Exiting Habit Tracker...")
            break
        else:
            print("Invalid option! Please try again.")


if __name__ == "__main__":
    main()






