habits = []

MILESTONES = [10, 25, 50, 100]


def add_habit():

    name = input("Enter habit name: ")

    habits.append({
        "name": name,
        "completion_count": 0,
        "milestones": []
    })

    print("Habit added successfully!")


def view_habits():

    if not habits:

        print("No habits available.")
        return

    print("\n===== HABITS =====")

    for index, habit in enumerate(habits, start=1):

        print(
            f"{index}. "
            f"{habit['name']} | "
            f"Completions: {habit['completion_count']}"
        )


def complete_habit():

    if not habits:

        print("No habits available.")
        return

    view_habits()

    try:

        choice = int(input("Enter habit number: "))

        if 1 <= choice <= len(habits):

            habit = habits[choice - 1]

            habit["completion_count"] += 1

            count = habit["completion_count"]

            if count in MILESTONES:

                habit["milestones"].append(count)

                print(f"🎉 Congratulations!")
                print(f"You unlocked the {count} completion milestone!")

            else:

                print("Habit completed successfully!")

        else:

            print("Invalid habit number.")

    except ValueError:

        print("Please enter a valid number.")


def view_milestones():

    if not habits:

        print("No habits available.")
        return

    print("\n===== MILESTONES =====")

    for habit in habits:

        print(f"\n{habit['name']}")

        if not habit["milestones"]:

            print("No milestones achieved yet.")

        else:

            for milestone in habit["milestones"]:

                print(f"🏆 {milestone} Completions")


while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. View Milestones")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        view_milestones()

    elif choice == "5":

        print("Goodbye!")
        break

    else:

        print("Invalid choice.")