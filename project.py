import sys
import json
import os
from datetime import date, timedelta


HABITS_FILE = "habits.json"


def main():
    if len(sys.argv) < 2:
        print("Usage: python project.py [add|check|streak|chart|list|delete] [habit]")
        sys.exit(1)

    command = sys.argv[1].lower()
    habit = sys.argv[2] if len(sys.argv) > 2 else None

    habits = load_habits()

    if command == "add":
        if not habit:
            sys.exit("Provide a habit name.")
        add_habit(habits, habit)

    elif command == "check":
        if not habit:
            sys.exit("Provide a habit name.")
        check_habit(habits, habit)

    elif command == "streak":
        if not habit:
            sys.exit("Provide a habit name.")
        s = get_streak(habits, habit)
        print(f"🔥 Current streak for '{habit}': {s} day(s)")

    elif command == "chart":
        if not habit:
            sys.exit("Provide a habit name.")
        print_chart(habits, habit)

    elif command == "list":
        list_habits(habits)

    elif command == "delete":
        if not habit:
            sys.exit("Provide a habit name.")
        delete_habit(habits, habit)

    else:
        sys.exit("Unknown command.")

    save_habits(habits)


def get_streak(habits, habit_name):
    """Calculate current consecutive day streak for a habit."""
    if habit_name not in habits:
        return 0

    completions = set(habits[habit_name]["completions"])
    streak = 0
    day = date.today()

    while str(day) in completions:
        streak += 1
        day -= timedelta(days=1)

    return streak


def get_chart_data(habits, habit_name, days=7):
    """Return list of 1s and 0s for last N days (1=done, 0=missed)."""
    if habit_name not in habits:
        return []

    completions = set(habits[habit_name]["completions"])
    result = []

    for i in range(days - 1, -1, -1):
        day = str(date.today() - timedelta(days=i))
        result.append(1 if day in completions else 0)

    return result


def format_streak_message(streak):
    """Return motivational message based on streak length."""
    if streak == 0:
        return "Start today — every streak begins with day 1!"
    elif streak < 3:
        return f"🌱 {streak} day(s) — keep going!"
    elif streak < 7:
        return f"🔥 {streak} days — you are building a habit!"
    elif streak < 30:
        return f"⚡ {streak} days — unstoppable!"
    else:
        return f"🏆 {streak} days — absolute legend!"


def load_habits():
    if os.path.exists(HABITS_FILE):
        with open(HABITS_FILE, "r") as f:
            return json.load(f)
    return {}


def save_habits(habits):
    with open(HABITS_FILE, "w") as f:
        json.dump(habits, f, indent=2)


def add_habit(habits, name):
    if name in habits:
        print(f"'{name}' already exists.")
        return
    habits[name] = {
        "created": str(date.today()),
        "completions": []
    }
    print(f"✅ Habit '{name}' added.")


def check_habit(habits, name):
    if name not in habits:
        print(f"'{name}' not found. Add it first.")
        return
    today = str(date.today())
    if today in habits[name]["completions"]:
        print(f"Already checked in '{name}' today!")
        return
    habits[name]["completions"].append(today)
    streak = get_streak(habits, name)
    print(f"✅ '{name}' checked for today!")
    print(format_streak_message(streak))


def delete_habit(habits, name):
    if name not in habits:
        print(f"'{name}' not found.")
        return
    del habits[name]
    print(f"🗑️  '{name}' deleted.")


def list_habits(habits):
    if not habits:
        print("No habits yet. Add one with: python project.py add 'HabitName'")
        return
    today = str(date.today())
    print(f"\n{'Habit':<20} {'Today':>8} {'Streak':>8}")
    print("-" * 38)
    for name, data in habits.items():
        done = "✅" if today in data["completions"] else "❌"
        streak = get_streak(habits, name)
        print(f"{name:<20} {done:>8} {streak:>7}🔥")


def print_chart(habits, name):
    if name not in habits:
        print(f"'{name}' not found.")
        return

    data = get_chart_data(habits, name, days=7)
    print(f"\n📊 Last 7 days — '{name}'")
    print()

    max_h = 5
    for row in range(max_h, 0, -1):
        line = ""
        for val in data:
            if val == 1:
                line += "███  "
            else:
                line += "░░░  "
        print(line)

    # day labels
    labels = ""
    for i in range(6, -1, -1):
        day = date.today() - timedelta(days=i)
        labels += day.strftime("%a") + "  "
    print(labels)
    print()


if __name__ == "__main__":
    main()