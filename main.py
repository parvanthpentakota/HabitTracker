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


def main():
    habits = []

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Delete Habit")
        print("5. Exit")

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
            print("Exiting...")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()






