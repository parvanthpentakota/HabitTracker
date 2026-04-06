from datetime import date

habits = ["Exercise", "Read", "Coding"]
completed = []

today = date.today()

print("=== Habit Tracker ===")
print("Date:", today)

# Show habits
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
                print(f"{habit} completed ✅")
            else:
                print("Already done ⚠")
        else:
            print("Invalid choice ❌")

    except ValueError:
        print("Enter valid number ❌")

# 🔥 Percentage Calculation
total = len(habits)
done = len(completed)

percentage = (done / total) * 100

print("\n=== Daily Progress ===")
print(f"Completed: {done}/{total}")
print(f"Progress: {round(percentage, 2)}%")

# 🔥 Feedback
if percentage == 100:
    print("🔥 Perfect Day!")
elif percentage >= 70:
    print("💪 Great job!")
elif percentage > 0:
    print("👍 Keep improving!")
else:
    print("⚠ Try to complete at least one habit!")