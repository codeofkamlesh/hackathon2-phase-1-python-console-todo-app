"""
Task model for the Todo App.

This module defines the Task dataclass that represents a single todo item
with fields for ID, title, description, and completion status.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Task:
    """
    Represents a single todo item in the system.

    Attributes:
        id (int): Unique identifier for the task, auto-incremented
        title (str): Required title of the task, maximum 200 characters
        description (str): Optional description of the task, maximum 1000 characters
        completed (bool): Status indicating whether the task is completed (default: False)
    """
    id: int
    title: str
    description: str = ""
    completed: bool = False

    def __post_init__(self):
        """Validate the task after initialization."""
        if not self.title.strip():
            raise ValueError("Task title cannot be empty or only whitespace")
        if len(self.title) > 200:
            raise ValueError("Task title cannot exceed 200 characters")
        if len(self.description) > 1000:
            raise ValueError("Task description cannot exceed 1000 characters")