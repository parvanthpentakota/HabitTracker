habits = ["Exercise", "Read", "Coding"]
completed = []

def mark_all_completed():
    for h in habits:
        if h not in completed:
            completed.append(h)
    print("All habits marked as completed ✅")

def show_status():
    print("\n=== Habit Status ===")
    for h in habits:
        status = "✅" if h in completed else "❌"
        print(f"{h} {status}")

def mark_single():
    for i, h in enumerate(habits, start=1):
        print(f"{i}. {h}")

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
    print("1. Mark One Habit")
    print("2. Mark All Habits ⚡")
    print("3. Show Status")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        mark_single()
    elif choice == "2":
        mark_all_completed()
    elif choice == "3":
        show_status()
    elif choice == "0":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option ❌")