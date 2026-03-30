from datetime import date

habits = ["Exercise", "Read", "Coding"]
completed = []

today = date.today()

def show_habits():
    print("\n=== Habits ===")
    for i, h in enumerate(habits, start=1):
        print(f"{i}. {h}")

def mark_completed():
    show_habits()
    try:
        choice = int(input("Enter habit number: "))
        if 1 <= choice <= len(habits):
            habit = habits[choice - 1]
            if habit not in completed:
                completed.append(habit)
                print("Marked as completed ✅")
            else:
                print("Already completed ⚠")
        else:
            print("Invalid choice ❌")
    except:
        print("Enter valid number ❌")

def add_habit():
    new_habit = input("Enter new habit: ")
    habits.append(new_habit)
    print("Habit added ✅")

def show_summary():
    print("\n=== Summary ===")
    print("Completed:", len(completed), "/", len(habits))
    for h in completed:
        print("-", h)

while True:
    print("\n=== Habit Tracker Menu ===")
    print("1. View Habits")
    print("2. Mark Completed")
    print("3. Add Habit")
    print("4. Show Summary")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_habits()
    elif choice == "2":
        mark_completed()
    elif choice == "3":
        add_habit()
    elif choice == "4":
        show_summary()
    elif choice == "0":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option ❌")