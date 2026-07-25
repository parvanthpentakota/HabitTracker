from datetime import datetime

habits = []

def add_habit():

    name = input("Enter habit name: ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")

    habits.append({
        "name": name,
        "deadline": deadline,
        "completed": False
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:

        print("No habits available.")
        return

    today = datetime.today().date()

    print("\n===== HABITS =====")

    for index, habit in enumerate(habits, start=1):

        deadline = datetime.strptime(
            habit["deadline"],
            "%Y-%m-%d"
        ).date()

        if habit["completed"]:

            status = "Completed"

        elif deadline < today:

            status = "Overdue"

        elif deadline == today:

            status = "Due Today"

        else:

            status = "Pending"

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Deadline: {habit['deadline']} | "
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

            print("Habit completed successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def check_overdue():

    today = datetime.today().date()

    print("\n===== OVERDUE HABITS =====")

    found = False

    for habit in habits:

        deadline = datetime.strptime(
            habit["deadline"],
            "%Y-%m-%d"
        ).date()

        if deadline < today and not habit["completed"]:

            print(
                f"{habit['name']} "
                f"(Deadline: {habit['deadline']})"
            )

            found = True

    if not found:

        print("No overdue habits.")

while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Overdue Habits")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        check_overdue()

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")