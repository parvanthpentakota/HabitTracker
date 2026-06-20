import sqlite3
import csv

# Database Setup
conn = sqlite3.connect("habits.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS habits(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE,
    streak INTEGER,
    completed INTEGER
)
""")
conn.commit()


def add_habit():

    habit_name = input("Enter habit name: ")

    try:

        cursor.execute(
            "INSERT INTO habits(name, streak, completed) VALUES(?,?,?)",
            (habit_name, 0, 0)
        )

        conn.commit()

        print("Habit added successfully!")

    except sqlite3.IntegrityError:

        print("Habit already exists.")


def view_habits():

    cursor.execute(
        "SELECT id, name, streak, completed FROM habits"
    )

    habits = cursor.fetchall()

    if not habits:

        print("No habits available.")
        return

    print("\n===== Habit Dashboard =====")

    for habit in habits:

        status = (
            "✅ Completed"
            if habit[3]
            else "❌ Pending"
        )

        print(
            f"{habit[0]}. "
            f"{habit[1]} | "
            f"Streak: {habit[2]} | "
            f"Status: {status}"
        )


def complete_habit():

    view_habits()

    try:

        habit_id = int(
            input("Enter habit ID to complete: ")
        )

        cursor.execute(
            """
            UPDATE habits
            SET streak = streak + 1,
                completed = 1
            WHERE id = ?
            """,
            (habit_id,)
        )

        conn.commit()

        print("Habit completed successfully!")

    except ValueError:

        print("Please enter a valid number.")


def show_longest_streak():

    cursor.execute(
        """
        SELECT name, streak
        FROM habits
        ORDER BY streak DESC
        LIMIT 1
        """
    )

    result = cursor.fetchone()

    if result:

        print("\n===== Longest Streak =====")
        print(
            f"Habit: {result[0]} | "
            f"Streak: {result[1]}"
        )

    else:

        print("No habits available.")


def rank_habits():

    cursor.execute(
        """
        SELECT name, streak
        FROM habits
        ORDER BY streak DESC
        """
    )

    habits = cursor.fetchall()

    print("\n===== Habit Ranking =====")

    for rank, habit in enumerate(
        habits,
        start=1
    ):

        print(
            f"{rank}. "
            f"{habit[0]} | "
            f"Streak: {habit[1]}"
        )


def show_progress():

    cursor.execute(
        "SELECT COUNT(*) FROM habits"
    )

    total = cursor.fetchone()[0]

    if total == 0:

        print("No habits available.")
        return

    cursor.execute(
        """
        SELECT COUNT(*)
        FROM habits
        WHERE completed = 1
        """
    )

    completed = cursor.fetchone()[0]

    progress = int(
        (completed / total) * 20
    )

    print("\n===== Daily Progress =====")

    print(
        "[" +
        "#" * progress +
        "-" * (20 - progress) +
        "]"
    )

    print(
        f"{completed}/{total} habits completed"
    )


def export_csv():

    cursor.execute(
        """
        SELECT name,
               streak,
               completed
        FROM habits
        """
    )

    habits = cursor.fetchall()

    with open(
        "habits.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Habit", "Streak", "Completed"]
        )

        writer.writerows(habits)

    print(
        "Habits exported to habits.csv"
    )


def reset_daily_status():

    cursor.execute(
        """
        UPDATE habits
        SET completed = 0
        """
    )

    conn.commit()

    print("Daily status reset.")


while True:

    print("\n===== Habit Tracker =====")
    print("1. Add Habit")
    print("2. View Habits")
    print("3. Complete Habit")
    print("4. Longest Streak")
    print("5. Rank Habits")
    print("6. Progress Dashboard")
    print("7. Export CSV")
    print("8. Reset Daily Status")
    print("9. Exit")

    choice = input(
        "Enter your choice: "
    )

    if choice == "1":

        add_habit()

    elif choice == "2":

        view_habits()

    elif choice == "3":

        complete_habit()

    elif choice == "4":

        show_longest_streak()

    elif choice == "5":

        rank_habits()

    elif choice == "6":

        show_progress()

    elif choice == "7":

        export_csv()

    elif choice == "8":

        reset_daily_status()

    elif choice == "9":

        print("Exiting Habit Tracker...")
        conn.close()
        break

    else:

        print("Invalid choice.")