from datetime import datetime

habits = ["Exercise", "Read", "Coding"]
completed = {}  # habit -> time

def show_habits():
    print("\n=== Habits ===")
    for i, h in enumerate(habits, start=1):
        if h in completed:
            print(f"{i}. {h} ✅ at {completed[h]}")
        else:
            print(f"{i}. {h} ❌")

def mark_completed():
    show_habits()
    try:
        choice = int(input("Enter habit number: "))
        if 1 <= choice <= len(habits):
            habit = habits[choice - 1]

            if habit not in completed:
                time_now = datetime.now().strftime("%H:%M:%S")
                completed[habit] = time_now
                print(f"{habit} completed at {time_now} ⏱️")
            else:
                print("Already completed ⚠")
        else:
            print("Invalid choice ❌")
    except:
        print("Enter valid number ❌")

def show_summary():
    print("\n=== Summary ===")
    for h, t in completed.items():
        print(f"{h} → completed at {t}")

while True:
    print("\n=== Habit Tracker ===")
    print("1. View Habits")
    print("2. Mark Completed ⏱️")
    print("3. Show Summary")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_habits()
    elif choice == "2":
        mark_completed()
    elif choice == "3":
        show_summary()
    elif choice == "0":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option ❌")