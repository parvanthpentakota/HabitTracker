# habit_tracker.py

from datetime import datetime

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habits.append({
        "name": habit_name,
        "streak": 0,
        "completed": False,
        "last_completed": "Never"
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:

        print("No habits available.")
        return

    print("\n===== Habit Dashboard =====")

    for index, habit in enumerate(habits, start=1):

        status = "✅ Completed" if habit["completed"] else "❌ Pending"

        print(
            f"{index}. "
            f"Habit: {habit['name']} | "
            f"Streak: {habit['streak']} | "
            f"Last Completed: {habit['last_completed']} | "
            f"Status: {status}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to complete: "))

        if 1 <= choice <= len(habits):

            selected = habits[choice - 1]

            if not selected["completed"]:

                selected["completed"] = True
                selected["streak"] += 1
                selected["last_completed"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                print("Habit completed successfully!")

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def view_last_completion():

    print("\n===== Last Completion Times =====")

    if not habits:

        print("No habits available.")
        return

    for habit in habits:

        print(
            f"{habit['name']} -> "
            f"{habit['last_completed']}"
        )

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Last Completion Times")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        view_last_completion()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")