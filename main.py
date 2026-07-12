# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")

    habits.append({
        "name": habit_name,
        "streak": 0,
        "completed": False,
        "favorite": False
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits available.")
        return

    print("\n===== Habit Dashboard =====")

    for index, habit in enumerate(habits, start=1):

        status = "✅ Completed" if habit["completed"] else "❌ Pending"
        favorite = "⭐" if habit["favorite"] else ""

        print(
            f"{index}. "
            f"{favorite} {habit['name']} | "
            f"Streak: {habit['streak']} | "
            f"Status: {status}"
        )

def mark_favorite():

    view_habits()

    try:

        choice = int(input("Enter habit number to mark as favorite: "))

        if 1 <= choice <= len(habits):

            habits[choice - 1]["favorite"] = True

            print("Habit marked as favorite!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def view_favorites():

    print("\n===== Favorite Habits =====")

    found = False

    for habit in habits:

        if habit["favorite"]:

            print(
                f"⭐ {habit['name']} | "
                f"Streak: {habit['streak']}"
            )

            found = True

    if not found:

        print("No favorite habits found.")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Favorite")
    print("4. View Favorite Habits")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        mark_favorite()

    elif option == "4":

        view_favorites()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")