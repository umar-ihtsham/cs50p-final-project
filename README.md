# CLI Habit Tracker

## Description
A command-line habit tracker that lets you build and monitor daily habits
with streak tracking and ASCII bar charts. Data persists in a local JSON file.

## Usage

python project.py add "Exercise"      # add a new habit
python project.py check "Exercise"    # mark today as complete
python project.py streak "Exercise"   # see current streak
python project.py chart "Exercise"    # ASCII chart of last 7 days
python project.py list                # all habits + today status
python project.py delete "Exercise"   # remove a habit

## Design Choices
- JSON for storage — human readable, no external dependencies
- Streak calculated backwards from today so gaps correctly break it
- ASCII chart chosen over external libraries to keep it dependency-free

## Files
- `project.py` — main program
- `test_project.py` — pytest tests
- `habits.json` — auto-generated data file