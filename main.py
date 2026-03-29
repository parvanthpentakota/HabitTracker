from datetime import date

FILE_NAME = "habits.txt"

today = str(date.today())
habits = ["Exercise", "Read", "Coding"]
completed = []

print("=== Habit Tracker ===")
print("Date:", today)

# 🔥 Load previous data
history = []
try:
    with open(FILE_NAME, "r") as file:
        history = file.readlines()
except FileNotFoundError:
    pass

# 🔥 Calculate streak (simple logic: count today's entries)
streak = 0
for line in history:
    if today in line:
        streak += 1

print(f"\n🔥 Current Streak Today: {streak}")

# Show habits
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
                print(f"{habit} completed ✅")
            else:
                print("Already done ⚠")
        else:
            print("Invalid choice ❌")

    except ValueError:
        print("Enter a valid number ❌")

# Save to file
with open(FILE_NAME, "a") as file:
    for habit in completed:
        file.write(f"{today} - {habit}\n")

# Final streak update
print("\n=== Summary ===")
print("Completed:", len(completed), "/", len(habits))
print("🔥 Updated Streak Today:", streak + len(completed))