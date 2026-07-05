# CLI Habit Tracker

#### Video Demo:https://youtu.be/Z3M35p-VHV0

#### GitHub:https://github.com/umar-ihtsham/cs50p-final-project

#### Description:

## What is this project?

CLI Habit Tracker is a command-line application built in Python that
helps users build and maintain daily habits. Instead of a complicated
app, it runs directly in the terminal with simple commands. The program
tracks which days you completed each habit, calculates your current
streak, and displays a visual ASCII bar chart of your last 7 days.

All data is saved locally in a JSON file called habits.json, which means
your habits and history persist between sessions without needing any
database or internet connection.

## Why I built it

Building good habits is one of the most impactful things a person can
do. Most habit tracking apps are overcomplicated or require you to sign
up for an account. This project aims to solve that by giving developers
and terminal users a lightweight, fast, dependency-free tool they can
actually use every day.

## How to use it

The program is run from the terminal using the following commands:

    python project.py add "Exercise"     — adds a new habit
    python project.py check "Exercise"   — marks today as complete
    python project.py streak "Exercise"  — shows current streak count
    python project.py chart "Exercise"   — ASCII chart of last 7 days
    python project.py list               — lists all habits and status
    python project.py delete "Exercise"  — removes a habit permanently

## Files in this project

### project.py
This is the main file containing all the logic. It contains the main()
function which reads sys.argv to determine which command the user typed
and calls the appropriate function.

The three required standalone functions are:

- get_streak(habits, habit_name): Calculates the current consecutive
  day streak for a habit by walking backwards from today and checking
  if each day exists in the completions list. The moment a day is
  missing, the streak stops.

- get_chart_data(habits, habit_name, days): Returns a list of 1s and
  0s representing the last N days. 1 means the habit was completed that
  day, 0 means it was missed. This data is used by print_chart() to
  draw the ASCII visualization.

- format_streak_message(streak): Takes an integer streak count and
  returns a motivational message appropriate to the streak length.
  Short streaks get encouraging messages, long streaks get celebratory
  ones. This function has no side effects — it purely returns a string.

Additional helper functions include load_habits(), save_habits(),
add_habit(), check_habit(), delete_habit(), list_habits(), and
print_chart(). These are all kept separate so each function does
exactly one thing, making the code easier to test and maintain.

### test_project.py
Contains 7 pytest test functions that test the three required standalone
functions. Each test builds a small habits dictionary in memory and
passes it directly to the function — no file system is touched during
testing. Tests cover edge cases like empty habits, broken streaks, and
habits checked today.

### habits.json
Auto-generated when you first add a habit. Stores all habit names,
creation dates, and completion dates as a JSON dictionary. Human
readable so you can inspect or edit it manually if needed.

### requirements.txt
Lists pytest as the only dependency. All other modules used (json, os,
sys, datetime) are part of Python's standard library.

## Design choices

### Why JSON instead of CSV?
JSON maps naturally to the nested data structure needed — each habit
has a name, a creation date, and a list of completion dates. CSV would
require multiple files or awkward flattening of that structure.

### Why command-line instead of a GUI?
A CLI tool starts instantly, works on any machine with Python, and fits
naturally into a developer's workflow. It can also be extended into
scripts and automation later.

### Why calculate streaks backwards from today?
Walking backwards from today and stopping at the first missing day is
the most accurate definition of a current streak. An alternative would
be to find the longest streak ever — but that is a different metric.
The current approach answers the question users actually care about:
how many days in a row have I done this up to today?

### Why store completions as a list of date strings?
ISO format date strings like "2024-01-15" are human readable, easily
comparable, and sortable without any conversion. Using date objects
would require serialization. Strings keep the JSON file clean and
readable.

## What I learned

This project taught me how to structure a real Python program with
multiple functions, write meaningful pytest tests, persist data with
JSON, and work with Python's datetime module to do date arithmetic.
It also reinforced the importance of keeping functions small and focused
so they are easy to test independently.
