# habit_tracker.py

habits = []

def add_habit():
    habit = input("Enter new habit: ")
    habits.append({"habit": habit, "completed": False})
    print("Habit added successfully!")

def view_habits():
    if not habits:
        print("No habits available.")
    else:
        print("\n===== Your Habits =====")
        for index, item in enumerate(habits, start=1):
            status = "✅ Completed" if item["completed"] else "❌ Pending"
            print(f"{index}. {item['habit']} - {status}")

def complete_habit():
    view_habits()

    try:
        choice = int(input("Enter habit number to mark complete: "))

        if 1 <= choice <= len(habits):
            habits[choice - 1]["completed"] = True
            print("Habit marked as completed!")
        else:
            print("Invalid habit number.")

    except ValueError:
        print("Please enter a valid number.")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_habit()

    elif option == "2":
        view_habits()

    elif option == "3":
        complete_habit()

    elif option == "4":
        print("Exiting Habit Tracker...")
        break

    else:
        print("Invalid option. Try again.")