from datetime import date

habits = ["Exercise", "Read", "Coding"]
completed = []

today = date.today()

def show_habits():
    print("\n=== Habits ===")
    for i, h in enumerate(habits, start=1):
        status = "✅" if h in completed else "❌"
        print(f"{i}. {h} {status}")

def mark_completed():
    show_habits()
    try:
        choice = int(input("Enter habit number: "))
        if 1 <= choice <= len(habits):
            habit = habits[choice - 1]
            completed.add(habit) if isinstance(completed, set) else completed.append(habit)
            print("Marked as completed ✅")
        else:
            print("Invalid choice ❌")
    except:
        print("Enter valid number ❌")

def undo_habit():
    show_habits()
    try:
        choice = int(input("Enter habit number to undo: "))
        if 1 <= choice <= len(habits):
            habit = habits[choice - 1]
            if habit in completed:
                completed.remove(habit)
                print("Habit undone 🔄")
            else:
                print("Habit not completed yet ⚠")
        else:
            print("Invalid choice ❌")
    except:
        print("Enter valid number ❌")

def summary():
    print("\n=== Summary ===")
    print("Completed:", len(completed), "/", len(habits))

while True:
    print("\n=== Habit Tracker ===")
    print("1. View Habits")
    print("2. Mark Completed")
    print("3. Undo Habit")
    print("4. Summary")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_habits()
    elif choice == "2":
        mark_completed()
    elif choice == "3":
        undo_habit()
    elif choice == "4":
        summary()
    elif choice == "0":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option ❌")