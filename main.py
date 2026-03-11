# Simple Habit Tracker

habits = ["Exercise", "Read 10 pages", "Practice coding"]

completed = []

print("Today's Habits:\n")

for i, habit in enumerate(habits, start=1):
    print(f"{i}. {habit}")

print("\nEnter the number of the habit you completed (0 to stop):")

while True:
    choice = int(input("Habit number: "))

    if choice == 0:
        break

    if 1 <= choice <= len(habits):
        completed.append(habits[choice - 1])
        print("Marked as completed!")
    else:
        print("Invalid choice")

print("\nCompleted Habits Today:")
for habit in completed:
    print("-", habit)

print("\nTotal completed:", len(completed))