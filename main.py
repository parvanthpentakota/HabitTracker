# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")
    category = input("Enter category (Health/Study/Fitness/etc.): ")

    habits.append({
        "name": habit_name,
        "category": category,
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
            f"Category: {habit['category']} | "
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

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def view_by_category():

    category = input("Enter category to filter: ").strip().lower()

    filtered = [
        habit for habit in habits
        if habit["category"].lower() == category
    ]

    if not filtered:

        print("No habits found in this category.")
        return

    print(f"\n===== {category.title()} Habits =====")

    for habit in filtered:

        status = "✅" if habit["completed"] else "❌"

        print(
            f"{habit['name']} | "
            f"Streak: {habit['streak']} | "
            f"{status}"
        )

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Habits by Category")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        view_by_category()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")