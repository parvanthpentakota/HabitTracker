# habit_tracker.py

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

            habit = habits[choice - 1]

            if not habit["completed"]:

                habit["completed"] = True
                habit["streak"] += 1

                print("Habit completed successfully!")

            else:

                print("Habit already completed.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def edit_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to edit: "))

        if 1 <= choice <= len(habits):

            new_name = input("Enter new habit name: ")

            habits[choice - 1]["name"] = new_name

            print("Habit updated successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def delete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to delete: "))

        if 1 <= choice <= len(habits):

            removed_habit = habits.pop(choice - 1)

            print(f"{removed_habit['name']} deleted successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def sort_habits_by_streak():

    if not habits:
        print("No habits available.")
        return

    sorted_habits = sorted(
        habits,
        key=lambda habit: habit["streak"],
        reverse=True
    )

    print("\n===== Habits Ranked By Streak =====")

    for habit in sorted_habits:

        print(
            f"{habit['name']} | "
            f"Streak: {habit['streak']}"
        )

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Edit Habit")
    print("5. Delete Habit")
    print("6. Rank Habits By Streak")
    print("7. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        edit_habit()

    elif option == "5":

        delete_habit()

    elif option == "6":

        sort_habits_by_streak()

    elif option == "7":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")