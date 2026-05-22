# habit_tracker.py

habits = []

def add_habit():

    name = input("Enter habit name: ")

    habit = {
        "name": name,
        "streak": 0,
        "completed": False
    }

    habits.append(habit)

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits found.")
        return

    print("\n===== Habit List =====")

    for index, habit in enumerate(habits, start=1):

        status = "Completed ✅" if habit["completed"] else "Pending ❌"

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

            habits[choice - 1]["completed"] = True
            habits[choice - 1]["streak"] += 1

            print("Habit marked as completed!")

        else:
            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def reset_habits():

    for habit in habits:

        habit["completed"] = False

    print("All habits reset for a new day!")

while True:

    print("\n===== Habit Tracker =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Reset Daily Status")
    print("5. Exit")

    option = input("Enter your option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        reset_habits()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Try again.")