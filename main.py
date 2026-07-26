habits = []
action_history = []


def add_habit():

    name = input("Enter habit name: ")

    habits.append({
        "name": name,
        "completed": False
    })

    print("Habit added successfully!")


def view_habits():

    if not habits:

        print("No habits available.")
        return

    print("\n===== HABITS =====")

    for index, habit in enumerate(habits, start=1):

        status = "Completed" if habit["completed"] else "Pending"

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

                print("Habit already completed.")
                return

            habit["completed"] = True

            action_history.append(choice - 1)

            print("Habit completed successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")


def undo_last_completion():

    if not action_history:

        print("Nothing to undo.")
        return

    last_index = action_history.pop()

    habits[last_index]["completed"] = False

    print(f"Undo successful: '{habits[last_index]['name']}' is now pending.")


while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Undo Last Completion")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        undo_last_completion()

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")