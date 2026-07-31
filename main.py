habits = []


def add_habit():

    name = input("Enter habit name: ")

    habits.append({
        "name": name,
        "current_streak": 0,
        "best_streak": 0,
        "completed_today": False
    })

    print("Habit added successfully!")


def view_habits():

    if not habits:

        print("No habits available.")
        return

    print("\n===== HABITS =====")

    for index, habit in enumerate(habits, start=1):

        status = (
            "Completed"
            if habit["completed_today"]
            else "Pending"
        )

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Current Streak: {habit['current_streak']} | "
            f"Best Streak: {habit['best_streak']} | "
            f"Status: {status}"
        )


def complete_habit():

    if not habits:

        print("No habits available.")
        return

    view_habits()

    try:

        choice = int(input("Enter habit number: "))

        if 1 <= choice <= len(habits):

            habit = habits[choice - 1]

            if habit["completed_today"]:

                print("Habit already completed today.")
                return

            habit["completed_today"] = True
            habit["current_streak"] += 1

            if habit["current_streak"] > habit["best_streak"]:

                habit["best_streak"] = habit["current_streak"]

                print("🎉 New personal best!")

            print("Habit completed successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")


def reset_day():

    if not habits:

        print("No habits available.")
        return

    for habit in habits:

        if not habit["completed_today"]:

            habit["current_streak"] = 0

        habit["completed_today"] = False

    print("New day started successfully!")


def show_best_records():

    if not habits:

        print("No habits available.")
        return

    print("\n===== PERSONAL BESTS =====")

    for habit in habits:

        print(
            f"{habit['name']} : "
            f"{habit['best_streak']} days"
        )


while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Start New Day")
    print("5. View Personal Bests")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        reset_day()

    elif choice == "5":

        show_best_records()

    elif choice == "6":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")