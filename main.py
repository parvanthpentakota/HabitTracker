from datetime import datetime

habits = []

def add_habit():

    name = input("Enter habit name: ")

    habits.append({
        "name": name,
        "completed": False,
        "monthly_count": {}
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

                print("Habit already completed today.")
                return

            habit["completed"] = True

            month = datetime.now().strftime("%B %Y")

            if month not in habit["monthly_count"]:

                habit["monthly_count"][month] = 0

            habit["monthly_count"][month] += 1

            print("Habit completed successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Enter a valid number.")

def monthly_statistics():

    if not habits:

        print("No habits available.")
        return

    print("\n===== MONTHLY STATISTICS =====")

    for habit in habits:

        print(f"\nHabit: {habit['name']}")

        if not habit["monthly_count"]:

            print("No monthly data available.")

        else:

            for month, count in habit["monthly_count"].items():

                print(f"{month}: {count} completion(s)")

while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Monthly Statistics")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        monthly_statistics()

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")