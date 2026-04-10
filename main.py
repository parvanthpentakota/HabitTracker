from datetime import date

habits = ["Exercise", "Read", "Coding"]
completed = []

today = date.today()

def search_habit():
    name = input("Enter habit to search: ")

    if name in habits:
        if name in completed:
            print(f"{name} exists and is completed ✅")
        else:
            print(f"{name} exists but not completed ❌")
    else:
        print("Habit not found ⚠")

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
    print("2. Search Habit 🔍")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        mark_completed()
    elif choice == "2":
        search_habit()
    elif choice == "0":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option ❌")