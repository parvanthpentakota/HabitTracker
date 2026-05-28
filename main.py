# habit_tracker.py

habit_records = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habit = {
        "name": habit_name,
        "streak": 0,
        "completed_today": False
    }

    habit_records.append(habit)

    print("Habit added successfully!")

def view_habits():

    if not habit_records:
        print("No habits available.")
        return

    print("\n===== Habit Tracker Dashboard =====")

    for index, habit in enumerate(habit_records, start=1):

        status = "✅ Completed" if habit["completed_today"] else "❌ Pending"

        print(
            f"{index}. "
            f"Habit: {habit['name']} | "
            f"Current Streak: {habit['streak']} | "
            f"Today's Status: {status}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to complete: "))

        if 1 <= choice <= len(habit_records):

            selected_habit = habit_records[choice - 1]

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

def reset_daily_status():

    for habit in habit_records:

        habit["completed_today"] = False

    print("Daily habit status reset successfully!")

def delete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to delete: "))

        if 1 <= choice <= len(habit_records):

            removed_habit = habit_records.pop(choice - 1)

            print(f"{removed_habit['name']} deleted successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Reset Daily Status")
    print("5. Delete Habit")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        reset_daily_status()

    elif option == "5":

        delete_habit()

    elif option == "6":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")