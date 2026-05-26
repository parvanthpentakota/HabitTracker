# habit_tracker.py

habit_list = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habit = {
        "name": habit_name,
        "streak": 0,
        "completed": False
    }

    habit_list.append(habit)

    print("Habit added successfully!")

def display_habits():

    if not habit_list:
        print("No habits added yet.")
        return

    print("\n===== Habit Dashboard =====")

    for index, habit in enumerate(habit_list, start=1):

        status = "✅ Completed" if habit["completed"] else "❌ Pending"

        print(
            f"{index}. "
            f"Habit: {habit['name']} | "
            f"Streak: {habit['streak']} | "
            f"Status: {status}"
        )

def complete_habit():

    display_habits()

    try:

        choice = int(input("Enter habit number to complete: "))

        if 1 <= choice <= len(habit_list):

            selected_habit = habit_list[choice - 1]

            if selected_habit["completed"]:

                print("Habit already completed today.")

            else:

                selected_habit["completed"] = True
                selected_habit["streak"] += 1

                print("Habit completed successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def reset_habits():

    for habit in habit_list:

        habit["completed"] = False

    print("All habits reset for the next day!")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Reset Habits")
    print("5. Exit")

    option = input("Enter your option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        display_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        reset_habits()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")
