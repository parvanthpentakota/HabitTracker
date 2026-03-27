from datetime import date

# File to store completed habits
FILE_NAME = "habits.txt"

today = date.today()
print("=== Habit Tracker ===")
print("Date:", today)

habits = ["Exercise", "Read", "Coding"]
completed = []

print("\nToday's Habits:")
for i, habit in enumerate(habits, start=1):
    print(f"{i}. {habit}")

print("\nEnter habit number to mark as completed")
print("Enter 0 to finish")

# Input loop
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
print("Completed Habits:")

for h in completed:
    print("-", h)

print("\nSaved to file:", FILE_NAME)