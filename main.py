import json

class Habit:
    def __init__(self, name, progress=0):
        self.name = name
        self.progress = progress

    def mark_done(self):
        self.progress += 1

    def to_dict(self):
        return {"name": self.name, "progress": self.progress}

    @staticmethod
    def from_dict(data):
        return Habit(data["name"], data["progress"])

    def __str__(self):
        return f"{self.name} → Days Completed: {self.progress}"


# -------- FILE HANDLING --------
FILE_NAME = "habits.json"

def save_habits(habits):
    with open(FILE_NAME, "w") as f:
        json.dump([h.to_dict() for h in habits], f)


def load_habits():
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return [Habit.from_dict(h) for h in data]
    except:
        return []


# -------- DISPLAY --------
def display_habits(habits):
    if not habits:
        print("No habits found.")
        return

    print("\nYour Habits:")
    for i, habit in enumerate(habits):
        print(f"{i + 1}. {habit}")


# -------- MAIN APP --------
def main():
    habits = load_habits()

    while True:
        print("\n=== Habit Tracker ===")
        print("1. Add Habit")
        print("2. Mark Habit as Done")
        print("3. View Habits")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter habit name: ")
            habits.append(Habit(name))
            save_habits(habits)
            print("Habit added!")

        elif choice == "2":
            display_habits(habits)
            try:
                index = int(input("Select habit number: ")) - 1
                habits[index].mark_done()
                save_habits(habits)
                print("Habit updated!")
            except:
                print("Invalid choice!")

        elif choice == "3":
            display_habits(habits)

        elif choice == "4":
            print("Saved & Exiting...")
            save_habits(habits)
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()


