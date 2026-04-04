from datetime import date

FILE_NAME = "daily_summary.txt"

today = str(date.today())

habits = ["Exercise", "Read", "Coding"]
completed = set()

print("=== Habit Tracker ===")
print("Date:", today)

# 🔥 Load today's previous progress
try:
    with open(FILE_NAME, "r") as file:
        for line in file:
            saved_date, habit = line.strip().split(" - ")
            if saved_date == today:
                completed.add(habit)
except FileNotFoundError:
    pass

print("\nLoaded Progress:", list(completed))

# Show habits
for i, habit in enumerate(habits, start=1):
    status = "✅" if habit in completed else "❌"
    print(f"{i}. {habit} {status}")

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
                completed.add(habit)
                print(f"{habit} completed ✅")
            else:
                print("Already done ⚠")
        else:
            print("Invalid choice ❌")

    except ValueError:
        print("Enter a valid number ❌")

# 🔥 Save updated progress
with open(FILE_NAME, "a") as file:
    for habit in completed:
        file.write(f"{today} - {habit}\n")

# Summary
print("\n=== Summary ===")
print("Completed:", len(completed), "/", len(habits))