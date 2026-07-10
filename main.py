# habit_tracker.py

habits = []
archived_habits = []

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
        print("No active habits available.")
        return

    print("\n===== Active Habits =====")

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

                print("Habit completed successfully!")

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def archive_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to archive: "))

        if 1 <= choice <= len(habits):

            archived_habits.append(
                habits.pop(choice - 1)
            )

            print("Habit archived successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def view_archived_habits():

    if not archived_habits:

        print("No archived habits.")
        return

    print("\n===== Archived Habits =====")

    for habit in archived_habits:

        print(
            f"{habit['name']} | "
            f"Final Streak: {habit['streak']}"
        )

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Archive Habit")
    print("5. View Archived Habits")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        archive_habit()

    elif option == "5":

        view_archived_habits()

    elif option == "6":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")