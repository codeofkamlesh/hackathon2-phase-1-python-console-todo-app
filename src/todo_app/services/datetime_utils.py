"""
Datetime utility functions for the Todo App.

This module provides utility functions for date/time parsing, interval calculations,
and recurrence pattern handling for the advanced features.
"""

from datetime import datetime, timedelta
import re


def validate_datetime_format(dt_str: str) -> bool:
    """
    Validate that the datetime string is in ISO format (YYYY-MM-DD HH:MM).

    Args:
        dt_str (str): The datetime string to validate

    Returns:
        bool: True if the format is valid, False otherwise

    Raises:
        ValueError: If the datetime string is not in the correct format
    """
    if dt_str is None:
        return True  # None is valid for optional datetime fields

    if not isinstance(dt_str, str):
        raise ValueError("Datetime must be a string or None")

    # ISO 8601 format: YYYY-MM-DD HH:MM
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$'
    if not re.match(pattern, dt_str):
        raise ValueError(f"Datetime must be in ISO format (YYYY-MM-DD HH:MM), got: {dt_str}")

    return True


def validate_date_format(date_str: str) -> bool:
    """
    Validate that the date string is in ISO format (YYYY-MM-DD).

    Args:
        date_str (str): The date string to validate

    Returns:
        bool: True if the format is valid, False otherwise

    Raises:
        ValueError: If the date string is not in the correct format
    """
    if date_str is None:
        return True  # None is valid for optional date fields

    if not isinstance(date_str, str):
        raise ValueError("Date must be a string or None")

    # ISO 8601 format: YYYY-MM-DD
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, date_str):
        raise ValueError(f"Date must be in ISO format (YYYY-MM-DD), got: {date_str}")

    return True


def calculate_next_occurrence(current_dt: str, recurrence_pattern: str) -> str:
    """
    Calculate the next occurrence datetime based on the recurrence pattern.

    Args:
        current_dt (str): The current datetime in ISO format (YYYY-MM-DD HH:MM)
        recurrence_pattern (str): The recurrence pattern ('daily', 'weekly', 'monthly')

    Returns:
        str: The next occurrence datetime in ISO format (YYYY-MM-DD HH:MM)

    Raises:
        ValueError: If the inputs are invalid
    """
    if not validate_datetime_format(current_dt):
        raise ValueError(f"Invalid datetime format: {current_dt}")

    if recurrence_pattern not in ["daily", "weekly", "monthly"]:
        raise ValueError(f"Invalid recurrence pattern: {recurrence_pattern}. Must be 'daily', 'weekly', or 'monthly'")

    # Parse the current datetime
    current_datetime = datetime.strptime(current_dt, "%Y-%m-%d %H:%M")

    # Calculate the next occurrence based on the pattern
    if recurrence_pattern == "daily":
        next_datetime = current_datetime + timedelta(days=1)
    elif recurrence_pattern == "weekly":
        next_datetime = current_datetime + timedelta(weeks=1)
    elif recurrence_pattern == "monthly":
        # Add approximately 30 days for monthly recurrence
        next_datetime = current_datetime + timedelta(days=30)
    else:
        # This shouldn't happen due to validation above, but just in case
        raise ValueError(f"Unsupported recurrence pattern: {recurrence_pattern}")

    return next_datetime.strftime("%Y-%m-%d %H:%M")


def calculate_next_date(current_date: str, recurrence_pattern: str) -> str:
    """
    Calculate the next occurrence date based on the recurrence pattern.

    Args:
        current_date (str): The current date in ISO format (YYYY-MM-DD)
        recurrence_pattern (str): The recurrence pattern ('daily', 'weekly', 'monthly')

    Returns:
        str: The next occurrence date in ISO format (YYYY-MM-DD)

    Raises:
        ValueError: If the inputs are invalid
    """
    if not validate_date_format(current_date):
        raise ValueError(f"Invalid date format: {current_date}")

    if recurrence_pattern not in ["daily", "weekly", "monthly"]:
        raise ValueError(f"Invalid recurrence pattern: {recurrence_pattern}. Must be 'daily', 'weekly', or 'monthly'")

    # Parse the current date
    current_datetime = datetime.strptime(current_date, "%Y-%m-%d")

    # Calculate the next occurrence based on the pattern
    if recurrence_pattern == "daily":
        next_datetime = current_datetime + timedelta(days=1)
    elif recurrence_pattern == "weekly":
        next_datetime = current_datetime + timedelta(weeks=1)
    elif recurrence_pattern == "monthly":
        # Add approximately 30 days for monthly recurrence
        next_datetime = current_datetime + timedelta(days=30)
    else:
        # This shouldn't happen due to validation above, but just in case
        raise ValueError(f"Unsupported recurrence pattern: {recurrence_pattern}")

    return next_datetime.strftime("%Y-%m-%d")


def is_overdue(task_due_datetime: str, current_time: datetime = None) -> bool:
    """
    Check if a task is overdue based on its due datetime.

    Args:
        task_due_datetime (str): The task's due datetime in ISO format (YYYY-MM-DD HH:MM)
        current_time (datetime): The current time to compare against (defaults to now)

    Returns:
        bool: True if the task is overdue, False otherwise
    """
    if task_due_datetime is None:
        return False  # Tasks without due datetime are not overdue

    if current_time is None:
        current_time = datetime.now()

    due_datetime = datetime.strptime(task_due_datetime, "%Y-%m-%d %H:%M")
    return due_datetime < current_time


def is_upcoming(task_due_datetime: str, hours_ahead: int = 24, current_time: datetime = None) -> bool:
    """
    Check if a task is upcoming based on its due datetime.

    Args:
        task_due_datetime (str): The task's due datetime in ISO format (YYYY-MM-DD HH:MM)
        hours_ahead (int): Number of hours ahead to consider as "upcoming" (default: 24)
        current_time (datetime): The current time to compare against (defaults to now)

    Returns:
        bool: True if the task is upcoming, False otherwise
    """
    if task_due_datetime is None:
        return False  # Tasks without due datetime are not upcoming

    if current_time is None:
        current_time = datetime.now()

    due_datetime = datetime.strptime(task_due_datetime, "%Y-%m-%d %H:%M")
    time_diff = due_datetime - current_time
    hours_diff = time_diff.total_seconds() / 3600

    return 0 <= hours_diff <= hours_ahead


def parse_datetime(datetime_str: str) -> datetime:
    """
    Parse a datetime string in ISO format (YYYY-MM-DD HH:MM) to a datetime object.

    Args:
        datetime_str (str): The datetime string to parse

    Returns:
        datetime: The parsed datetime object

    Raises:
        ValueError: If the datetime string is not in the correct format
    """
    if datetime_str is None:
        raise ValueError("Cannot parse None datetime")

    try:
        return datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
    except ValueError:
        raise ValueError(f"Unable to parse datetime string: {datetime_str}. Expected format: YYYY-MM-DD HH:MM")


def is_overdue(task_due_datetime: str, current_time: datetime = None) -> bool:
    """
    Check if a task is overdue based on its due datetime.

    Args:
        task_due_datetime (str): The task's due datetime in ISO format (YYYY-MM-DD HH:MM)
        current_time (datetime): The current time to compare against (defaults to now)

    Returns:
        bool: True if the task is overdue, False otherwise
    """
    if task_due_datetime is None:
        return False  # Tasks without due datetime are not overdue

    if current_time is None:
        current_time = datetime.now()

    due_datetime = datetime.strptime(task_due_datetime, "%Y-%m-%d %H:%M")
    return due_datetime < current_time


def is_upcoming(task_due_datetime: str, hours_ahead: int = 24, current_time: datetime = None) -> bool:
    """
    Check if a task is upcoming based on its due datetime.

    Args:
        task_due_datetime (str): The task's due datetime in ISO format (YYYY-MM-DD HH:MM)
        hours_ahead (int): Number of hours ahead to consider as "upcoming" (default: 24)
        current_time (datetime): The current time to compare against (defaults to now)

    Returns:
        bool: True if the task is upcoming, False otherwise
    """
    if task_due_datetime is None:
        return False  # Tasks without due datetime are not upcoming

    if current_time is None:
        current_time = datetime.now()

    due_datetime = datetime.strptime(task_due_datetime, "%Y-%m-%d %H:%M")
    time_diff = due_datetime - current_time
    hours_diff = time_diff.total_seconds() / 3600

    return 0 <= hours_diff <= hours_ahead


def parse_date(date_str: str) -> datetime:
    """
    Parse a date string in ISO format (YYYY-MM-DD) to a datetime object.

    Args:
        date_str (str): The date string to parse

    Returns:
        datetime: The parsed datetime object (time set to 00:00:00)

    Raises:
        ValueError: If the date string is not in the correct format
    """
    if date_str is None:
        raise ValueError("Cannot parse None date")

    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"Unable to parse date string: {date_str}. Expected format: YYYY-MM-DD")