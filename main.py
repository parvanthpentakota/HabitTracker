# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habits.append({
        "name": habit_name,
        "completed": False,
        "streak": 0
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

                print("Habit completed successfully!")

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def check_daily_goal():

    if not habits:

        print("No habits available.")
        return

    completed = sum(
        1 for habit in habits
        if habit["completed"]
    )

    total = len(habits)

    print("\n===== Daily Goal Status =====")
    print(f"Completed: {completed}/{total}")

    if completed == total:

        print("🎉 Congratulations! You completed all your habits today!")

    else:

        remaining = total - completed

        print(f"You have {remaining} habit(s) remaining today.")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Check Daily Goal")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        check_daily_goal()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")