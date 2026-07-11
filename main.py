# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")
    tags = input(
        "Enter tags (comma separated): "
    )

    tag_list = [
        tag.strip().lower()
        for tag in tags.split(",")
        if tag.strip()
    ]

    habits.append({
        "name": habit_name,
        "tags": tag_list,
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

        status = (
            "✅ Completed"
            if habit["completed"]
            else "❌ Pending"
        )

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Tags: {', '.join(habit['tags'])} | "
            f"Streak: {habit['streak']} | "
            f"Status: {status}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(
            input("Enter habit number: ")
        )

        if 1 <= choice <= len(habits):

            habit = habits[choice - 1]

            if not habit["completed"]:

                habit["completed"] = True
                habit["streak"] += 1

                print(
                    "Habit completed successfully!"
                )

            else:

                print(
                    "Habit already completed."
                )

        else:

            print("Invalid habit number.")

    except ValueError:

        print(
            "Please enter a valid number."
        )

def search_by_tag():

    tag = input(
        "Enter tag to search: "
    ).strip().lower()

    found = False

    print("\n===== Matching Habits =====")

    for habit in habits:

        if tag in habit["tags"]:

            print(
                f"{habit['name']} | "
                f"Streak: {habit['streak']}"
            )

            found = True

    if not found:

        print(
            "No habits found with this tag."
        )

while True:

    print("\n===== Habit Tracker =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Search by Tag")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        search_by_tag()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option.")