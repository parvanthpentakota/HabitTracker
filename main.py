from datetime import date

# Show today's date
today = date.today()
print("Habit Tracker")
print("Date:", today)

# Habit list
habits = ["Exercise", "Read 10 pages", "Practice coding"]

completed = []

print("\nToday's Habits:\n")

# Display habits
for i, habit in enumerate(habits, start=1):
    print(f"{i}. {habit}")

print("\nEnter the number of the habit you completed")
print("Enter 99 to mark all as completed")
print("Enter 0 to stop")

# Mark completed habits
while True:
    choice = int(input("Habit number: "))

    if choice == 0:
        break

    if choice == 99:
        completed = habits.copy()
        print("All habits marked as completed!")
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

# Results
print("\nCompleted Habits Today:")
for habit in completed:
    print("-", habit)

# Calculations
total = len(habits)
done = len(completed)
remaining = total - done

progress = (done / total) * 100 if total > 0 else 0

print("\nTotal completed:", done)
print("Remaining habits:", remaining)
print("Progress:", round(progress, 2), "% completed")