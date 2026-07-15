# habit_tracker.py

habits = []

def add_habit():

    habit_name = input("Enter habit name: ")
    difficulty = input("Enter difficulty (Easy/Medium/Hard): ").capitalize()

    habits.append({
        "name": habit_name,
        "difficulty": difficulty,
        "streak": 0,
        "completed": False
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:

        print("No habits available.")
        return

    print("\n===== Habit Dashboard =====")

    for index, habit in enumerate(habits, start=1):

        status = "✅ Completed" if habit["completed"] else "❌ Pending"

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Difficulty: {habit['difficulty']} | "
            f"Streak: {habit['streak']} | "
            f"Status: {status}"
        )

def complete_habit():

    view_habits()

    try:

        choice = int(input("Enter habit number to complete: "))

        if 1 <= choice <= len(habits):

            selected = habits[choice - 1]

            if not selected["completed"]:

                selected["completed"] = True
                selected["streak"] += 1

                print("Habit completed successfully!")

            else:

                print("Habit already completed today.")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")

def difficulty_summary():

    easy = 0
    medium = 0
    hard = 0

    for habit in habits:

        if habit["difficulty"] == "Easy":
            easy += 1

        elif habit["difficulty"] == "Medium":
            medium += 1

        elif habit["difficulty"] == "Hard":
            hard += 1

    print("\n===== Difficulty Summary =====")
    print(f"Easy Habits   : {easy}")
    print(f"Medium Habits : {medium}")
    print(f"Hard Habits   : {hard}")

while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Difficulty Summary")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":

        add_habit()

    elif option == "2":

        view_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        difficulty_summary()

    elif option == "5":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Please try again.")