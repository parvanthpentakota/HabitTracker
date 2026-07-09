# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habits.append({
        "name": habit_name,
        "completed_days": 0,
        "total_days": 0
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits available.")
        return

    print("\n===== Habit Dashboard =====")

    for index, habit in enumerate(habits, start=1):

        percentage = 0

        if habit["total_days"] > 0:

            percentage = (
                habit["completed_days"] /
                habit["total_days"]
            ) * 100

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Completed: {habit['completed_days']} | "
            f"Tracked: {habit['total_days']} | "
            f"Success: {percentage:.2f}%"
        )

def update_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number: "))

        if 1 <= choice <= len(habits):

            completed = input(
                "Completed today? (y/n): "
            ).lower()

            selected = habits[choice - 1]

            selected["total_days"] += 1

            if completed == "y":

                selected["completed_days"] += 1

            print("Habit updated successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def show_best_habit():

    if not habits:

        print("No habits available.")
        return

    best = max(
        habits,
        key=lambda h: (
            h["completed_days"] /
            h["total_days"]
            if h["total_days"] > 0
            else 0
        )
    )

    percentage = (
        best["completed_days"] /
        best["total_days"]
    ) * 100 if best["total_days"] > 0 else 0

    print("\n===== Best Habit =====")
    print(
        f"Habit: {best['name']}"
    )
    print(
        f"Success Rate: {percentage:.2f}%"
    )

while True:

    print("\n===== Habit Tracker =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Update Today's Status")
    print("4. Best Performing Habit")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        update_habit()

    elif option == "4":

        show_best_habit()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option.")