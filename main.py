# habit_tracker.py

habits = []

def add_habit():
    habit_name = input("Enter habit name: ")

    habit = {
        "name": habit_name,
        "streak": 0,
        "completed": False
    }

    habits.append(habit)

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits available.")
        return

    print("\n===== Habit Dashboard =====")

    for index, habit in enumerate(habits, start=1):

        status = "✅ Done" if habit["completed"] else "❌ Pending"

        print(
            f"{index}. {habit['name']} | "
            f"Status: {status} | "
            f"Streak: {habit['streak']}"
        )

def complete_habit():

    view_habits()

    try:
        choice = int(input("Select habit number to complete: "))

        if 1 <= choice <= len(habits):

            habits[choice - 1]["completed"] = True
            habits[choice - 1]["streak"] += 1

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

    option = input("Enter your option: ")

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
        print("Invalid option. Try again.")