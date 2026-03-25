from datetime import date

# Display today's date
today = date.today()
print("=== Habit Tracker ===")
print("Date:", today)

# Habit list
habits = ["Exercise", "Read", "Coding"]

completed = []

print("\nToday's Habits:")
for i, habit in enumerate(habits, start=1):
    print(f"{i}. {habit}")

print("\nEnter habit number to mark as completed")
print("Enter 0 to finish")

while True:
    try:
        choice = int(input("Choice: "))

        if choice == 0:
            break

        if 1 <= choice <= len(habits):
            habit = habits[choice - 1]

            if habit not in completed:
                completed.append(habit)
                print(f"{habit} marked as completed ✅")
            else:
                print("Already completed ⚠")
        else:
            print("Invalid choice ❌")

    except ValueError:
        print("Enter a valid number ❌")

# Summary
print("\n=== Summary ===")
print("Completed Habits:")

for h in completed:
    print("-", h)

total = len(habits)
done = len(completed)

print("\nProgress:", (done / total) * 100, "%")
