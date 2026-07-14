# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habits.append({
        "name": habit_name,
        "completed_count": 0,
        "completed_today": False
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits available.")
        return

    print("\n===== Habit Dashboard =====")

    for index, habit in enumerate(habits, start=1):

        status = (
            "✅ Completed"
            if habit["completed_today"]
            else "❌ Pending"
        )

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Total Completions: {habit['completed_count']} | "
            f"Status: {status}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to complete: "))

        if 1 <= choice <= len(habits):

            selected_habit = habits[choice - 1]

            if not selected_habit["completed_today"]:

                selected_habit["completed_today"] = True
                selected_habit["completed_count"] += 1

                print("Habit completed successfully!")

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def show_leaderboard():

    if not habits:

        print("No habits available.")
        return

    ranking = sorted(
        habits,
        key=lambda habit: habit["completed_count"],
        reverse=True
    )

    print("\n===== Habit Leaderboard =====")

    for rank, habit in enumerate(ranking, start=1):

        print(
            f"{rank}. "
            f"{habit['name']} | "
            f"Completions: {habit['completed_count']}"
        )

def reset_daily_status():

    for habit in habits:

        habit["completed_today"] = False

    print("Daily status has been reset.")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Leaderboard")
    print("5. Reset Daily Status")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        show_leaderboard()

    elif option == "5":

        reset_daily_status()

    elif option == "6":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")