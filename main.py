# habit_tracker.py

habit_tracker = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habit = {
        "name": habit_name,
        "completed_days": 0,
        "completed_today": False
    }

    habit_tracker.append(habit)

    print("Habit added successfully!")

def view_habits():

    if not habit_tracker:
        print("No habits available.")
        return

    print("\n===== Habit Tracker Dashboard =====")

    for index, habit in enumerate(habit_tracker, start=1):

        status = "✅ Completed" if habit["completed_today"] else "❌ Pending"

        print(
            f"{index}. "
            f"Habit: {habit['name']} | "
            f"Days Completed: {habit['completed_days']} | "
            f"Today's Status: {status}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to complete: "))

        if 1 <= choice <= len(habit_tracker):

            selected_habit = habit_tracker[choice - 1]

            if not selected_habit["completed_today"]:

                selected_habit["completed_today"] = True
                selected_habit["completed_days"] += 1

                print("Habit completed successfully!")

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def reset_daily_progress():

    for habit in habit_tracker:

        habit["completed_today"] = False

    print("Daily progress has been reset!")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Reset Daily Progress")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        reset_daily_progress()

    elif option == "5":

        print("Closing Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")