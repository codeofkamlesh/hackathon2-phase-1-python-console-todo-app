"""
TodoManager service for the Todo App.

This module provides the core business logic for managing tasks,
including adding, retrieving, updating, deleting, and marking tasks
as complete or incomplete.
"""

from typing import Dict, List, Optional
from todo_app.models.task import Task
from todo_app.utils.validators import validate_title, validate_description, validate_task_id


class TodoManager:
    """
    Core service class for managing todo tasks with in-memory storage.

    This class handles all business logic for task management operations
    and is designed with extensibility in mind to support future features
    like priority, due_date, etc. without breaking existing functionality.
    """

    def __init__(self):
        """Initialize the TodoManager with empty storage."""
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str = "", **kwargs) -> int:
        """
        Add a new task to the todo list.

        Args:
            title (str): The title of the task (required)
            description (str): The description of the task (optional, default is empty string)
            **kwargs: Additional fields for future extensibility (e.g., priority, due_date)

        Returns:
            int: The ID of the newly created task

        Raises:
            ValueError: If the title is invalid or too long
        """
        # Validate inputs
        validate_title(title)
        validate_description(description)

        # Create a new task with the next available ID
        task_id = self._next_id
        self._next_id += 1

        # For extensibility, we could expand this to handle additional fields in the future
        task = Task(
            id=task_id,
            title=title,
            description=description,
            completed=False
        )

        # Add the task to the storage
        self._tasks[task_id] = task

        return task_id

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the todo list.

        Returns:
            List[Task]: A list of all tasks
        """
        return list(self._tasks.values())

    def get_task_by_id(self, task_id: int) -> Task:
        """
        Get a specific task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Task: The task with the specified ID

        Raises:
            ValueError: If the task ID doesn't exist
        """
        validated_id = validate_task_id(task_id)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        return self._tasks[validated_id]

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None, **kwargs) -> bool:
        """
        Update an existing task.

        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): New title (if provided)
            description (Optional[str]): New description (if provided)
            **kwargs: Additional fields for future extensibility

        Returns:
            bool: True if the task was successfully updated, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist or if provided values are invalid
        """
        validated_id = validate_task_id(task_id)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        task = self._tasks[validated_id]

        # Update fields if provided
        if title is not None:
            validate_title(title)
            task.title = title

        if description is not None:
            validate_description(description)
            task.description = description

        # Future: Handle additional fields from kwargs for extensibility

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete

        Returns:
            bool: True if the task was successfully deleted, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist
        """
        validated_id = validate_task_id(task_id)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        del self._tasks[validated_id]
        return True

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id (int): The ID of the task to mark as complete

        Returns:
            bool: True if the task was successfully marked as complete, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist
        """
        validated_id = validate_task_id(task_id)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        self._tasks[validated_id].completed = True
        return True

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id (int): The ID of the task to mark as incomplete

        Returns:
            bool: True if the task was successfully marked as incomplete, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist
        """
        validated_id = validate_task_id(task_id)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        self._tasks[validated_id].completed = False
        return True

    def get_next_id(self) -> int:
        """
        Get the next available ID for a new task.

        Returns:
            int: The next available ID
        """
        return self._next_id

    def get_task_count(self) -> int:
        """
        Get the total number of tasks.

        Returns:
            int: The number of tasks in the system
        """
        return len(self._tasks)