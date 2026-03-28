from datetime import date

FILE_NAME = "habits.txt"

today = date.today()
print("=== Habit Tracker ===")
print("Date:", today)

habits = ["Exercise", "Read", "Coding"]
completed = []

# 🔥 NEW: Show previous history
print("\n=== Previous History ===")
try:
    with open(FILE_NAME, "r") as file:
        data = file.readlines()
        if data:
            for line in data[-5:]:  # show last 5 entries
                print(line.strip())
        else:
            print("No history found")
except FileNotFoundError:
    print("No history file yet")

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

# Summary
print("\n=== Summary ===")
print("Completed:", len(completed), "/", len(habits))

print("\nSaved successfully ✅")