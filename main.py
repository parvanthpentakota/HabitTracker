habits = ["Exercise", "Read", "Coding"]
completed = []

def show_habits():
    print("\n=== Habits ===")
    for i, h in enumerate(habits, start=1):
        status = "✅" if h in completed else "❌"
        print(f"{i}. {h} {status}")

def edit_habit():
    show_habits()
    try:
        choice = int(input("Enter habit number to edit: "))
        if 1 <= choice <= len(habits):
            old_habit = habits[choice - 1]
            new_name = input("Enter new habit name: ")

            habits[choice - 1] = new_name

            # Update completed list if needed
            if old_habit in completed:
                completed.remove(old_habit)
                completed.append(new_name)

            print("Habit updated ✏️")
        else:
            print("Invalid choice ❌")
    except:
        print("Enter valid number ❌")

def mark_completed():
    show_habits()
    try:
        choice = int(input("Enter habit number: "))
        if 1 <= choice <= len(habits):
            habit = habits[choice - 1]
            if habit not in completed:
                completed.append(habit)
                print("Completed ✅")
            else:
                print("Already done ⚠")
        else:
            print("Invalid choice ❌")
    except:
        print("Enter valid number ❌")

while True:
    print("\n=== Habit Tracker ===")
    print("1. View Habits")
    print("2. Mark Completed")
    print("3. Edit Habit ✏️")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_habits()
    elif choice == "2":
        mark_completed()
    elif choice == "3":
        edit_habit()
    elif choice == "0":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option ❌")