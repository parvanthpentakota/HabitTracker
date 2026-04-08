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

# 🔥 NEW: Reset feature
def reset_day():
    completed.clear()
    print("Today's progress has been reset 🔄")

def summary():
    print("\n=== Summary ===")
    print("Completed:", len(completed), "/", len(habits))

while True:
    print("\n=== Habit Tracker ===")
    print("1. View Habits")
    print("2. Mark Completed")
    print("3. Reset Day 🔄")
    print("4. Summary")
    print("0. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        show_habits()
    elif choice == "2":
        show_habits()
        mark_completed()
    elif choice == "3":
        reset_day()
    elif choice == "4":
        summary()
    elif choice == "0":
        print("Goodbye 👋")
        break
    else:
        print("Invalid option ❌")