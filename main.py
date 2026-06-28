# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")
    category = input("Enter category (Health/Study/Fitness/Coding): ")

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

            selected = habits[choice - 1]

            if not selected["completed"]:

                selected["completed"] = True
                selected["streak"] += 1

                print("Habit completed successfully!")

            else:

                print("Habit already completed.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def view_by_category():

    category = input("Enter category to view: ").lower()

    print(f"\n===== {category.title()} Habits =====")

    found = False

    for habit in habits:

        if habit["category"].lower() == category:

            status = "✅" if habit["completed"] else "❌"

            print(
                f"{habit['name']} | "
                f"Streak: {habit['streak']} | "
                f"{status}"
            )

            found = True

    if not found:

        print("No habits found in this category.")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View All Habits")
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