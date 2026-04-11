habits = ["Exercise", "Read", "Coding"]
completed = []

def show_sorted_habits():
    sorted_list = sorted(habits)
    print("\n=== Sorted Habits ===")
    for h in sorted_list:
        status = "✅" if h in completed else "❌"
        print(f"{h} {status}")

def mark_completed():
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
    print("1. Mark Completed")
    print("2. View Sorted Habits 🔤")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        mark_completed()
    elif choice == "2":
        show_sorted_habits()
    elif choice == "0":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option ❌")