# habit_tracker.py

import time

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habits.append({
        "name": habit_name,
        "streak": 0,
        "completed": False
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
            f"{habit['name']} | "
            f"Streak: {habit['streak']} | "
            f"Status: {status}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to complete: "))

        if 1 <= choice <= len(habits):

            habits[choice - 1]["completed"] = True
            habits[choice - 1]["streak"] += 1

            print("Habit completed successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def remind_habits():

    print("\n===== Habit Reminder =====")

    pending = [
        habit["name"]
        for habit in habits
        if not habit["completed"]
    ]

    if not pending:

        print("🎉 All habits completed today!")

    else:

        for habit in pending:

            print(f"⏰ Don't forget: {habit}")

        print("\nReminder shown at:", time.strftime("%H:%M:%S"))

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Show Reminders")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        remind_habits()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")