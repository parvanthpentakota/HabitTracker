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

        choice = int(input("Enter habit number: "))

        if 1 <= choice <= len(habits):

            today = datetime.now().strftime("%Y-%m-%d")

            habit = habits[choice - 1]

            if today not in habit["history"]:

                habit["history"].append(today)

                print("Habit completed successfully!")

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Enter a valid number.")

def show_heatmap():

    if not habits:

        print("No habits available.")
        return

    view_habits()

    try:

        choice = int(input("Select habit number: "))

        if 1 <= choice <= len(habits):

            habit = habits[choice - 1]

            print(f"\n===== 30-Day Heatmap: {habit['name']} =====")

            for day in range(1, 31):

                date = datetime.now().replace(day=day).strftime("%Y-%m-%d")

                if date in habit["history"]:

                    print("🟩", end=" ")

                else:

                    print("⬜", end=" ")

                if day % 7 == 0:

                    print()

            print()

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Enter a valid number.")

while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Show 30-Day Heatmap")
    print("5. Exit")

    option = input("Enter your choice: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        show_heatmap()

    elif option == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")