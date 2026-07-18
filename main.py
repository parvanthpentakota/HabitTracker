habits = []

def add_habit():
    name = input("Enter habit name: ")

    habits.append({
        "name": name,
        "completed": False,
        "notes": []
    })

    print("Habit added successfully!")

def view_habits():

    if not habits:
        print("No habits found.")
        return

    print("\n===== HABITS =====")

    for i, habit in enumerate(habits, start=1):

        status = "Completed" if habit["completed"] else "Pending"

        print(f"{i}. {habit['name']} ({status})")

def complete_habit():

    view_habits()

    if not habits:
        return

    choice = int(input("Enter habit number: "))

    if 1 <= choice <= len(habits):
        habits[choice - 1]["completed"] = True
        print("Habit marked as completed.")
    else:
        print("Invalid choice.")

def add_note():

    view_habits()

    if not habits:
        return

    choice = int(input("Select habit number: "))

    if 1 <= choice <= len(habits):

        note = input("Write your note: ")

        habits[choice - 1]["notes"].append(note)

        print("Note added successfully!")

    else:
        print("Invalid choice.")

def view_notes():

    view_habits()

    if not habits:
        return

    choice = int(input("Select habit number: "))

    if 1 <= choice <= len(habits):

        notes = habits[choice - 1]["notes"]

        print(f"\nNotes for {habits[choice-1]['name']}:")

        if not notes:
            print("No notes available.")
        else:
            for i, note in enumerate(notes, start=1):
                print(f"{i}. {note}")

    else:
        print("Invalid choice.")

while True:

    print("\n===== HABIT TRACKER =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Add Note")
    print("5. View Notes")
    print("6. Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_habit()

    elif option == "2":
        view_habits()

    elif option == "3":
        complete_habit()

    elif option == "4":
        add_note()

    elif option == "5":
        view_notes()

    elif option == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")