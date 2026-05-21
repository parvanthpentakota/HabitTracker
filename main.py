# habit_tracker.py

# List to store all habits
habit_data = []

# Function to add a new habit
def add_habit():

    # Take habit name from user
    habit_name = input("Enter habit name: ")

    # Create a dictionary for one habit
    habit = {
        "name": habit_name,
        "completed_days": 0,
        "status": "Pending"
    }

    # Add habit dictionary into list
    habit_data.append(habit)

    print("Habit added successfully!")


# Function to display all habits
def show_habits():

    # Check if list is empty
    if not habit_data:
        print("No habits available.")
        return

    print("\n===== Habit Progress =====")

    # Loop through habits
    for index, habit in enumerate(habit_data, start=1):

        print(
            f"{index}. "
            f"Habit: {habit['name']} | "
            f"Completed Days: {habit['completed_days']} | "
            f"Status: {habit['status']}"
        )


# Function to mark habit as completed
def complete_habit():

    # First display all habits
    show_habits()

    try:

        # User selects habit number
        choice = int(input("Enter habit number to complete: "))

        # Validate choice
        if 1 <= choice <= len(habit_data):

            # Update selected habit
            habit_data[choice - 1]["completed_days"] += 1
            habit_data[choice - 1]["status"] = "Completed ✅"

            print("Habit marked as completed!")

        else:
            print("Invalid habit number.")

    except ValueError:

        # Handle invalid number input
        print("Please enter a valid number.")


# Main program loop
while True:

    print("\n===== Habit Tracker Menu =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Exit")

    # Take menu option
    option = input("Enter your choice: ")

    # Menu conditions
    if option == "1":

        add_habit()

    elif option == "2":

        show_habits()

    elif option == "3":

        complete_habit()

    elif option == "4":

        print("Exiting Habit Tracker...")
        break

    else:

        print("Invalid option. Try again.")