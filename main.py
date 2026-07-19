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

    view_habits()

    if not habits:
        return

    try:

        choice = int(input("Enter habit number: "))

        if 1 <= choice <= len(habits):

            habits[choice - 1]["completed"] = True

            print("Habit marked as completed.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def search_habit():

    if not habits:

        print("No habits available.")
        return

    keyword = input("Enter keyword to search: ").lower()

    found = False

    print("\n===== SEARCH RESULTS =====")

    for index, habit in enumerate(habits, start=1):

        if keyword in habit["name"].lower():

            status = "Completed" if habit["completed"] else "Pending"

            print(f"{index}. {habit['name']} - {status}")

            found = True

    if not found:

        print("No matching habits found.")

while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Search Habit")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        search_habit()

    elif choice == "5":

        print("Thank you for using Habit Tracker!")

        break

    else:

        print("Invalid choice.")