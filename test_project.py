import pytest
from project import get_streak, get_chart_data, format_streak_message
from datetime import date, timedelta


def test_get_streak_empty():
    habits = {}
    assert get_streak(habits, "Exercise") == 0


def test_get_streak_active():
    today = str(date.today())
    yesterday = str(date.today() - timedelta(days=1))
    habits = {
        "Exercise": {
            "created": yesterday,
            "completions": [yesterday, today]
        }
    }
    assert get_streak(habits, "Exercise") == 2


def test_get_streak_broken():
    today = str(date.today())
    two_days_ago = str(date.today() - timedelta(days=2))
    habits = {
        "Exercise": {
            "created": two_days_ago,
            "completions": [two_days_ago, today]  
        }
    }
    assert get_streak(habits, "Exercise") == 1


def test_chart_data_length():
    today = str(date.today())
    habits = {"Read": {"created": today, "completions": [today]}}
    data = get_chart_data(habits, "Read", days=7)
    assert len(data) == 7


def test_chart_data_today_done():
    today = str(date.today())
    habits = {"Read": {"created": today, "completions": [today]}}
    data = get_chart_data(habits, "Read", days=7)
    assert data[-1] == 1   


def test_format_streak_zero():
    assert "Start" in format_streak_message(0)


def test_format_streak_high():
    assert "30" in format_streak_message(30) or "legend" in format_streak_message(30)