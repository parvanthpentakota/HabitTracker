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

            selected_habit = habits[choice - 1]

            if not selected_habit["completed"]:

                selected_habit["completed"] = True
                selected_habit["streak"] += 1

                print("Habit completed successfully!")

            else:

                print("Habit already completed.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def view_statistics():

    if not habits:
        print("No habits available.")
        return

    total_habits = len(habits)

    completed_habits = sum(
        1 for habit in habits
        if habit["completed"]
    )

    completion_rate = (
        completed_habits / total_habits
    ) * 100

    print("\n===== Habit Statistics =====")
    print(f"Total Habits: {total_habits}")
    print(f"Completed Habits: {completed_habits}")
    print(f"Completion Rate: {completion_rate:.2f}%")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Statistics")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        view_statistics()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")
