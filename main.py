# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")

    new_habit = {
        "name": habit_name,
        "streak": 0,
        "completed_today": False
    }

    habits.append(new_habit)

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits available.")
        return

    print("\n===== Habit Overview =====")

    for index, habit in enumerate(habits, start=1):

        status = "✅ Done" if habit["completed_today"] else "❌ Pending"

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

            selected_habit = habits[choice - 1]

            if selected_habit["completed_today"]:

                print("Habit already completed today.")

            else:

                selected_habit["completed_today"] = True
                selected_habit["streak"] += 1

                print("Habit marked as completed!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def reset_day():

    for habit in habits:

        habit["completed_today"] = False

    print("Daily habit status reset successfully!")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Reset Daily Status")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        reset_day()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Try again.")
