# habit_tracker.py

habits = {}

while True:
    print("\n===== Habit Tracker =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Mark Habit Complete")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        habit_name = input("Enter habit name: ")

        if habit_name in habits:
            print("Habit already exists!")
        else:
            habits[habit_name] = False
            print(f"{habit_name} added successfully.")

    elif choice == "2":

        if not habits:
            print("No habits found.")
        else:
            print("\nYour Habits:")
            for habit, status in habits.items():
                status_text = "Completed ✅" if status else "Pending ❌"
                print(f"- {habit}: {status_text}")

    elif choice == "3":

        habit_name = input("Enter habit name to mark complete: ")

        if habit_name in habits:
            habits[habit_name] = True
            print(f"{habit_name} marked as completed.")
        else:
            print("Habit not found.")

    elif choice == "4":
        print("Exiting Habit Tracker...")
        break

    else:
        print("Invalid choice. Please try again.")