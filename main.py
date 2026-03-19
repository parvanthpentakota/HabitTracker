from datetime import date

today = date.today()
print("Habit Tracker")
print("Date:", today)

habits = ["Exercise", "Read 10 pages", "Practice coding"]
completed = []

print("\nToday's Habits:\n")

for i, habit in enumerate(habits, start=1):
    print(f"{i}. {habit}")

print("\nEnter the number of the habit you completed")
print("Enter 0 to stop")

while True:
    try:
        choice = int(input("Habit number: "))

        if choice == 0:
            break

        if 1 <= choice <= len(habits):
            habit_name = habits[choice - 1]

            if habit_name not in completed:
                completed.append(habit_name)
                print("Marked as completed!")
            else:
                print("Already completed!")
        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter a valid number!")

print("\nCompleted Habits Today:")
for habit in completed:
    print("-", habit)

total = len(habits)
done = len(completed)

print("\nTotal completed:", done)
