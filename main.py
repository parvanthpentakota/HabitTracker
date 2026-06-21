# habit_tracker.py

import json

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habits.append({
        "name": habit_name,
        "streak": 0,
        "completed": False
    })

    print("Habit added successfully!")

def save_habits():

    with open("habits.json", "w") as file:

        json.dump(
            habits,
            file,
            indent=4
        )

    print("Habits saved successfully!")

def load_habits():

    global habits

    try:

        with open("habits.json", "r") as file:

            habits = json.load(file)

        print("Habits loaded successfully!")

    except FileNotFoundError:

        print("No saved habits found.")

def view_habits():

    if not habits:

        print("No habits available.")
        return

    print("\n===== Habit Dashboard =====")

    for index, habit in enumerate(habits, start=1):

        status = (
            "✅ Completed"
            if habit["completed"]
            else "❌ Pending"
        )

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Streak: {habit['streak']} | "
            f"Status: {status}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(
            input(
                "Enter habit number to complete: "
            )
        )

        if 1 <= choice <= len(habits):

            habits[choice - 1]["completed"] = True
            habits[choice - 1]["streak"] += 1

            print(
                "Habit completed successfully!"
            )

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

while True:

    print("\n===== Habit Tracker =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Save Habits")
    print("5. Load Habits")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        save_habits()

    elif option == "5":

        load_habits()

    elif option == "6":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option.")
