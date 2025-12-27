"""
Task model for the Todo App.

This module defines the Task dataclass that represents a single todo item
with fields for ID, title, description, completion status, priority, tags, and due date.
"""

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Task:
    """
    Represents a single todo item in the system.

    Attributes:
        id (int): Unique identifier for the task, auto-incremented
        title (str): Required title of the task, maximum 200 characters
        description (str): Optional description of the task, maximum 1000 characters
        completed (bool): Status indicating whether the task is completed (default: False)
        priority (str): Priority level of the task (default: 'medium', values: 'high', 'medium', 'low')
        tags (List[str]): List of tags associated with the task (default: [])
        due_date (Optional[str]): Due date in ISO format (YYYY-MM-DD) or None (default: None)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "medium"
    tags: List[str] = None
    due_date: Optional[str] = None

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title.strip():
            raise ValueError("Task title cannot be empty or only whitespace")
        if len(self.title) > 200:
            raise ValueError("Task title cannot exceed 200 characters")
        if len(self.description) > 1000:
            raise ValueError("Task description cannot exceed 1000 characters")

        # Initialize tags as empty list if not provided
        if self.tags is None:
            self.tags = []

        # Validate priority
        if self.priority not in ["high", "medium", "low"]:
            raise ValueError(f"Priority must be one of 'high', 'medium', or 'low', got: {self.priority}")

        # Validate tags
        if not isinstance(self.tags, list):
            raise ValueError("Tags must be a list of strings")
        for tag in self.tags:
            if not isinstance(tag, str):
                raise ValueError(f"All tags must be strings, got: {type(tag)} for tag: {tag}")

        # Validate due date format if provided
        if self.due_date is not None:
            self._validate_due_date_format(self.due_date)

    def _validate_due_date_format(self, due_date: str) -> bool:
        """Validate that the due date is in ISO format (YYYY-MM-DD)."""
        import re
        # ISO 8601 format: YYYY-MM-DD
        pattern = r'^\d{4}-\d{2}-\d{2}$'
        if not re.match(pattern, due_date):
            raise ValueError(f"Due date must be in ISO format (YYYY-MM-DD), got: {due_date}")
        return True