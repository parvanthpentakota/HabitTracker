# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()

    habits.append({
        "name": habit_name,
        "priority": priority,
        "streak": 0,
        "completed": False
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits available.")
        return

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3
    }

    sorted_habits = sorted(
        habits,
        key=lambda habit: priority_order.get(
            habit["priority"],
            4
        )
    )

    print("\n===== Habit Dashboard =====")

    for index, habit in enumerate(sorted_habits, start=1):

        status = (
            "✅ Completed"
            if habit["completed"]
            else "❌ Pending"
        )

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Priority: {habit['priority']} | "
            f"Streak: {habit['streak']} | "
            f"Status: {status}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to complete: "))

        priority_order = {
            "High": 1,
            "Medium": 2,
            "Low": 3
        }

        sorted_habits = sorted(
            habits,
            key=lambda habit: priority_order.get(
                habit["priority"],
                4
            )
        )

        if 1 <= choice <= len(sorted_habits):

            selected = sorted_habits[choice - 1]

            selected["completed"] = True
            selected["streak"] += 1

            print("Habit completed successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")