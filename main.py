# habit_tracker.py

habits = []

def add_habit():
    name = input("Enter habit name: ")

    habit = {
        "name": name,
        "streak": 0,
        "completed": False
    }

    habits.append(habit)
    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits available.")
        return

    print("\n===== Habit Summary =====")

    for index, habit in enumerate(habits, start=1):

        status = "✅ Completed" if habit["completed"] else "❌ Pending"

        print(
            f"{index}. {habit['name']} | "
            f"Streak: {habit['streak']} | "
            f"Status: {status}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number: "))

        if 1 <= choice <= len(habits):

            habits[choice - 1]["completed"] = True
            habits[choice - 1]["streak"] += 1

            print("Habit completed successfully!")

        else:
            print("Invalid habit number.")

    except ValueError:
        print("Please enter a valid number.")

def show_statistics():

    total = len(habits)

    completed = sum(
        1 for habit in habits
        if habit["completed"]
    )

    print("\n===== Statistics =====")
    print(f"Total Habits: {total}")
    print(f"Completed Today: {completed}")
    print(f"Pending: {total - completed}")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Statistics")
    print("5. Exit")

    option = input("Enter your choice: ")

    if option == "1":
        add_habit()

    elif option == "2":
        view_habits()

    elif option == "3":
        complete_habit()

    elif option == "4":
        show_statistics()

    elif option == "5":
        print("Exiting Habit Tracker...")
        break

    else:
        print("Invalid choice. Try again.")