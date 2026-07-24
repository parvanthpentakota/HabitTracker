habits = []

def add_habit():

    name = input("Enter habit name: ")
    category = input("Enter category (Health/Study/Fitness/Work/Personal): ")

    habits.append({
        "name": name,
        "category": category,
        "completed": False
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits available.")
        return

    print("\n===== ALL HABITS =====")

    for index, habit in enumerate(habits, start=1):

        status = "Completed" if habit["completed"] else "Pending"

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Category: {habit['category']} | "
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

            habits[choice - 1]["completed"] = True

            print("Habit marked as completed.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def filter_by_category():

    if not habits:
        print("No habits available.")
        return

    category = input("Enter category to search: ").strip().lower()

    print(f"\n===== {category.title()} HABITS =====")

    found = False

    for habit in habits:

        if habit["category"].lower() == category:

            status = "Completed" if habit["completed"] else "Pending"

            print(
                f"{habit['name']} | "
                f"Status: {status}"
            )

            found = True

    if not found:

        print("No habits found in this category.")

while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Filter by Category")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        filter_by_category()

    elif choice == "5":

        print("Thank you for using Habit Tracker!")
        break

    else:

        print("Invalid choice.")