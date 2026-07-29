from datetime import datetime

habits = []


def add_habit():

    name = input("Enter habit name: ")

    habits.append({
        "name": name,
        "time_stats": {
            "Morning": 0,
            "Afternoon": 0,
            "Evening": 0,
            "Night": 0
        }
    })

    print("Habit added successfully!")


def view_habits():

    if not habits:

        print("No habits available.")
        return

    print("\n===== HABITS =====")

    for index, habit in enumerate(habits, start=1):

        print(f"{index}. {habit['name']}")


def get_time_period():

    hour = datetime.now().hour

    if 5 <= hour < 12:

        return "Morning"

    elif 12 <= hour < 17:

        return "Afternoon"

    elif 17 <= hour < 21:

        return "Evening"

    else:

        return "Night"


def complete_habit():

    if not habits:

        print("No habits available.")
        return

    view_habits()

    try:

        choice = int(input("Enter habit number: "))

        if 1 <= choice <= len(habits):

            habit = habits[choice - 1]

            period = get_time_period()

            habit["time_stats"][period] += 1

            print(f"Habit completed during {period}!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")


def view_time_statistics():

    if not habits:

        print("No habits available.")
        return

    print("\n===== TIME ANALYTICS =====")

    for habit in habits:

        print(f"\nHabit: {habit['name']}")

        for period, count in habit["time_stats"].items():

            print(f"{period}: {count}")


while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Time Analytics")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        view_time_statistics()

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid option.")