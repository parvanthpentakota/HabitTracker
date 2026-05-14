# habit_tracker.py

habits = []

while True:
    print("\n=== Habit Tracker ===")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        habit = input("Enter habit name: ")
        habits.append({"name": habit, "completed": False})
        print("Habit added successfully!")

    elif choice == "2":
        if not habits:
            print("No habits added yet.")
        else:
            print("\nYour Habits:")
            for index, habit in enumerate(habits, start=1):
                status = "✅" if habit["completed"] else "❌"
                print(f"{index}. {habit['name']} - {status}")

    elif choice == "3":
        if not habits:
            print("No habits available.")
        else:
            for index, habit in enumerate(habits, start=1):
                print(f"{index}. {habit['name']}")

            try:
                habit_index = int(input("Enter habit number to mark completed: ")) - 1

                if 0 <= habit_index < len(habits):
                    habits[habit_index]["completed"] = True
                    print("Habit marked as completed!")
                else:
                    print("Invalid habit number.")

            except ValueError:
                print("Please enter a valid number.")

    elif choice == "4":
        print("Exiting Habit Tracker...")
        break

    else:
        print("Invalid choice. Try again.")