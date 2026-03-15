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

print("\nEnter the number of the habit you completed (0 to stop):")

# Mark completed habits
while True:
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

# Results
print("\nCompleted Habits Today:")
for habit in completed:
    print("-", habit)

# Calculations
total_habits = len(habits)
completed_count = len(completed)
remaining = total_habits - completed_count

# Progress percentage
if total_habits > 0:
    progress = (completed_count / total_habits) * 100
else:
    progress = 0

print("\nTotal completed:", completed_count)
print("Remaining habits:", remaining)
print("Progress:", round(progress, 2), "% completed")

# Simple Habit Tracker - Daily Summary

habits = ["Exercise", "Read 10 pages", "Practice coding"]

completed = ["Exercise", "Practice coding"]

print("Today's Habits:")
for habit in habits:
    print("-", habit)

print("\nCompleted Habits:")
for habit in completed:
    print("-", habit)

total = len(habits)
done = len(completed)

print("\nSummary")
print("Total habits:", total)
print("Completed:", done)
print("Remaining:", total - done)