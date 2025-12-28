"""
Input validation utilities for the Todo App.

This module provides validation functions for task titles, descriptions,
and other user inputs to ensure they meet the required criteria.
"""

import re
from typing import Union


def validate_title(title: str) -> bool:
    """
    Validate a task title.

    Args:
        title (str): The title to validate

    Returns:
        bool: True if the title is valid, False otherwise

    Raises:
        ValueError: If the title is invalid
    """
    if not isinstance(title, str):
        raise ValueError("Title must be a string")

    if not title or not title.strip():
        raise ValueError("Task title cannot be empty or only whitespace")

    if len(title) > 200:
        raise ValueError("Task title cannot exceed 200 characters")

    return True


def validate_description(description: str) -> bool:
    """
    Validate a task description.

    Args:
        description (str): The description to validate

    Returns:
        bool: True if the description is valid, False otherwise

    Raises:
        ValueError: If the description is invalid
    """
    if not isinstance(description, str):
        raise ValueError("Description must be a string")

    if len(description) > 1000:
        raise ValueError("Task description cannot exceed 1000 characters")

    return True


def validate_task_id(task_id: Union[int, str]) -> int:
    """
    Validate a task ID.

    Args:
        task_id (Union[int, str]): The task ID to validate

    Returns:
        int: The validated task ID as an integer

    Raises:
        ValueError: If the task ID is invalid
    """
    if isinstance(task_id, str):
        try:
            task_id = int(task_id)
        except ValueError:
            raise ValueError(f"Task ID must be a valid integer, got: {task_id}")

    if not isinstance(task_id, int):
        raise ValueError(f"Task ID must be an integer, got: {type(task_id).__name__}")

    if task_id <= 0:
        raise ValueError(f"Task ID must be a positive integer, got: {task_id}")

    return task_id


def validate_priority(priority: str) -> bool:
    """
    Validate a task priority.

    Args:
        priority (str): The priority to validate

    Returns:
        bool: True if the priority is valid, False otherwise

    Raises:
        ValueError: If the priority is invalid
    """
    if not isinstance(priority, str):
        raise ValueError("Priority must be a string")

    if priority not in ["high", "medium", "low"]:
        raise ValueError(f"Priority must be one of 'high', 'medium', or 'low', got: {priority}")

    return True


def validate_tags(tags: list) -> bool:
    """
    Validate a list of task tags.

    Args:
        tags (list): The list of tags to validate

    Returns:
        bool: True if the tags are valid, False otherwise

    Raises:
        ValueError: If the tags are invalid
    """
    if not isinstance(tags, list):
        raise ValueError("Tags must be a list")

    for tag in tags:
        if not isinstance(tag, str):
            raise ValueError(f"All tags must be strings, got: {type(tag)} for tag: {tag}")

    return True


def validate_due_date(due_date: str) -> bool:
    """
    Validate a due date string in ISO format.

    Args:
        due_date (str): The due date string to validate in ISO format (YYYY-MM-DD)

    Returns:
        bool: True if the due date is valid, False otherwise

    Raises:
        ValueError: If the due date is invalid
    """
    if due_date is None:
        return True  # None is valid for due_date

    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string or None")

    import re
    # ISO 8601 format: YYYY-MM-DD
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, due_date):
        raise ValueError(f"Due date must be in ISO format (YYYY-MM-DD), got: {due_date}")

    return True


def validate_due_datetime(due_datetime: str) -> bool:
    """
    Validate a due datetime string in ISO format.

    Args:
        due_datetime (str): The due datetime string to validate in ISO format (YYYY-MM-DD HH:MM)

    Returns:
        bool: True if the due datetime is valid, False otherwise

    Raises:
        ValueError: If the due datetime is invalid
    """
    if due_datetime is None:
        return True  # None is valid for due_datetime

    if not isinstance(due_datetime, str):
        raise ValueError("Due datetime must be a string or None")

    import re
    # ISO 8601 format: YYYY-MM-DD HH:MM
    pattern = r'^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$'
    if not re.match(pattern, due_datetime):
        raise ValueError(f"Due datetime must be in ISO format (YYYY-MM-DD HH:MM), got: {due_datetime}")

    return True


def sanitize_input(input_str: str) -> str:
    """
    Sanitize user input to prevent injection attacks.

    Args:
        input_str (str): The input string to sanitize

    Returns:
        str: The sanitized input string
    """
    if not isinstance(input_str, str):
        return str(input_str) if input_str is not None else ""

    # Remove any potential harmful characters or patterns
    # For now, we'll just return the string as Python strings are generally safe
    # In a more complex system, we might want to do more thorough sanitization
    return input_str