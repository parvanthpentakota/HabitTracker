habits = []

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

            habits[choice - 1]["completed"] = True

            print("Habit marked as completed.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def show_completion_percentage():

    if not habits:

        print("No habits available.")
        return

    completed = 0

    for habit in habits:

        if habit["completed"]:

            completed += 1

    percentage = (completed / len(habits)) * 100

    print("\n===== DAILY PROGRESS =====")
    print(f"Completed Habits : {completed}")
    print(f"Total Habits     : {len(habits)}")
    print(f"Completion Rate  : {percentage:.2f}%")

while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Show Completion Percentage")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        show_completion_percentage()

    elif choice == "5":

        print("Goodbye!")

        break

    else:

        print("Invalid choice.")
