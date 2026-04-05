from datetime import date

FILE_NAME = "habits.txt"

print("=== Weekly Habit Report ===")

weekly_data = {}

# Read file
try:
    with open(FILE_NAME, "r") as file:
        for line in file:
            d, habit = line.strip().split(" - ")

            if d not in weekly_data:
                weekly_data[d] = []

            weekly_data[d].append(habit)

except FileNotFoundError:
    print("No data available yet")
    exit()

# Display report
total = 0

print("\n=== Weekly Summary ===")

for day in weekly_data:
    count = len(weekly_data[day])
    total += count

    print(f"{day}: {count} habits completed")

print("\nTotal Habits Completed This Week:", total)