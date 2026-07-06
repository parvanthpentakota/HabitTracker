# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")
    goal = int(input("Enter target streak: "))

    habits.append({
        "name": habit_name,
        "streak": 0,
        "goal": goal,
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

        progress = (
            f"{habit['streak']}/{habit['goal']}"
        )

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Progress: {progress} | "
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

                if selected["streak"] >= selected["goal"]:

                    print(
                        f"🎉 Goal achieved for "
                        f"{selected['name']}!"
                    )

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def reset_daily_status():

    for habit in habits:

        habit["completed"] = False

    print("Daily status reset successfully!")

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

        reset_daily_status()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")