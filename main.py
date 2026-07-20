import csv

habits = []

def add_habit():

    name = input("Enter habit name: ")

    habits.append({
        "name": name,
        "completed": False,
        "streak": 0
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:

        print("No habits found.")
        return

    print("\n===== HABITS =====")

    for index, habit in enumerate(habits, start=1):

        status = "Completed" if habit["completed"] else "Pending"

        print(
            f"{index}. {habit['name']} | "
            f"Status: {status} | "
            f"Streak: {habit['streak']}"
        )

def complete_habit():

    view_habits()

    if not habits:
        return

    try:

        choice = int(input("Enter habit number: "))

        if 1 <= choice <= len(habits):

            if not habits[choice - 1]["completed"]:

                habits[choice - 1]["completed"] = True
                habits[choice - 1]["streak"] += 1

                print("Habit completed!")

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Enter a valid number.")

def export_csv():

    if not habits:

        print("No habits to export.")
        return

    with open("habit_report.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Habit Name",
            "Completed",
            "Streak"
        ])

        for habit in habits:

            writer.writerow([
                habit["name"],
                habit["completed"],
                habit["streak"]
            ])

    print("Habit report exported successfully!")
    print("File created: habit_report.csv")

while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Export CSV Report")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        export_csv()

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid option.")
