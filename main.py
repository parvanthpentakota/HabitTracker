# habit_tracker.py

habit_tracker = {}

def add_habit():
    habit = input("Enter habit name: ")

    if habit in habit_tracker:
        print("Habit already exists.")
    else:
        habit_tracker[habit] = "Pending"
        print("Habit added successfully!")

def view_habits():

    if not habit_tracker:
        print("No habits found.")
        return

    print("\n===== Habit List =====")

    for index, (habit, status) in enumerate(habit_tracker.items(), start=1):
        print(f"{index}. {habit} -> {status}")

def complete_habit():

    habit = input("Enter habit name to mark complete: ")

    if habit in habit_tracker:
        habit_tracker[habit] = "Completed ✅"
        print("Habit marked as completed!")
    else:
        print("Habit not found.")

while True:

    print("\n===== Habit Tracker =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_habit()

    elif choice == "2":
        view_habits()

    elif choice == "3":
        complete_habit()

    elif choice == "4":
        print("Closing Habit Tracker...")
        break

    else:
        print("Invalid choice. Try again.")