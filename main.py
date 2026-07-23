from datetime import datetime

habits = []

def add_habit():

    name = input("Enter habit name: ")

    habits.append({
        "name": name,
        "completed": False,
        "history": []
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits available.")
        return

    print("\n===== HABITS =====")

    for index, habit in enumerate(habits, start=1):

        status = "✅ Completed" if habit["completed"] else "❌ Pending"

        print(f"{index}. {habit['name']} - {status}")

def complete_habit():

    if not habits:
        print("No habits available.")
        return

    view_habits()

    try:

        choice = int(input("Enter habit number: "))

        if 1 <= choice <= len(habits):

            habit = habits[choice - 1]

            if habit["completed"]:

                print("Habit already completed today.")
                return

            habit["completed"] = True

            completion_time = datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            habit["history"].append(completion_time)

            print("Habit completed successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Enter a valid number.")

def view_history():

    if not habits:
        print("No habits available.")
        return

    view_habits()

    try:

        choice = int(input("Select habit number: "))

        if 1 <= choice <= len(habits):

            habit = habits[choice - 1]

            print(f"\n===== History of {habit['name']} =====")

            if not habit["history"]:

                print("No completion history available.")

            else:

                for index, record in enumerate(habit["history"], start=1):

                    print(f"{index}. {record}")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Enter a valid number.")

while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Completion History")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        view_history()

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")