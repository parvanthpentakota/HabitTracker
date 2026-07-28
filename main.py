from calendar import monthrange
from datetime import datetime

habits = []

def add_habit():

    name = input("Enter habit name: ")

    habits.append({
        "name": name,
        "history": []
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:

        print("No habits available.")
        return

    print("\n===== HABITS =====")

    for index, habit in enumerate(habits, start=1):

        print(f"{index}. {habit['name']}")

def complete_habit():

    if not habits:

        print("No habits available.")
        return

    view_habits()

    try:

        choice = int(input("Select habit number: "))

        if 1 <= choice <= len(habits):

            today = datetime.now().strftime("%Y-%m-%d")

            if today not in habits[choice - 1]["history"]:

                habits[choice - 1]["history"].append(today)

                print("Habit completed!")

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def show_calendar():

    if not habits:

        print("No habits available.")
        return

    view_habits()

    try:

        choice = int(input("Select habit number: "))

        if not (1 <= choice <= len(habits)):

            print("Invalid habit number.")
            return

        year = int(input("Enter year (YYYY): "))
        month = int(input("Enter month (1-12): "))

        days = monthrange(year, month)[1]

        habit = habits[choice - 1]

        print(f"\n===== {habit['name']} Calendar =====")

        for day in range(1, days + 1):

            date = f"{year}-{month:02d}-{day:02d}"

            if date in habit["history"]:

                print(f"{day:02d} ✅")

            else:

                print(f"{day:02d} ❌")

    except ValueError:

        print("Invalid input.")

while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Show Monthly Calendar")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        show_calendar()

    elif option == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid option.")