# habit_tracker.py

from datetime import datetime

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habits.append({
        "name": habit_name,
        "streak": 0,
        "completed": False,
        "completion_dates": []
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

            selected = habits[choice - 1]

            if not selected["completed"]:

                selected["completed"] = True
                selected["streak"] += 1

                today = datetime.now().strftime("%Y-%m-%d")

                selected["completion_dates"].append(today)

                print("Habit completed successfully!")

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def view_completion_calendar():

    view_habits()

    try:

        choice = int(input("Enter habit number: "))

        if 1 <= choice <= len(habits):

            selected = habits[choice - 1]

            print(f"\n===== Completion Calendar: {selected['name']} =====")

            if not selected["completion_dates"]:

                print("No completion records available.")

            else:

                for date in selected["completion_dates"]:

                    print(f"✅ {date}")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Completion Calendar")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        view_completion_calendar()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")