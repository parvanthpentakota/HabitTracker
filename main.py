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
        print("No habits found.")
        return

    print("\n===== Habit Dashboard =====")

    for index, habit in enumerate(habits, start=1):

        status = "✅ Done" if habit["completed"] else "❌ Pending"

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

def longest_streak():

    if not habits:
        print("No habits available.")
        return

    best_habit = max(habits, key=lambda habit: habit["streak"])

    print("\n===== Longest Streak =====")
    print(
        f"Habit: {best_habit['name']} | "
        f"Streak: {best_habit['streak']} days"
    )

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Longest Streak")
    print("5. Exit")

    option = input("Enter your choice: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        longest_streak()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid choice. Please try again.")