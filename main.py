# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habit = {
        "name": habit_name,
        "completed_days": 0,
        "status": "Pending"
    }

    habits.append(habit)

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits available.")
        return

    print("\n===== Habit Tracker Dashboard =====")

    for index, habit in enumerate(habits, start=1):

        print(
            f"{index}. "
            f"Habit: {habit['name']} | "
            f"Completed Days: {habit['completed_days']} | "
            f"Status: {habit['status']}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to complete: "))

        if 1 <= choice <= len(habits):

            selected_habit = habits[choice - 1]

            selected_habit["completed_days"] += 1
            selected_habit["status"] = "Completed ✅"

            print("Habit marked as completed!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def remove_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to remove: "))

        if 1 <= choice <= len(habits):

            removed_habit = habits.pop(choice - 1)

            print(f"{removed_habit['name']} removed successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Remove Habit")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        remove_habit()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Try again.")