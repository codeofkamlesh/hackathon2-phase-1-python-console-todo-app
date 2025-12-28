"""
TodoManager service for the Todo App.

This module provides the core business logic for managing tasks,
including adding, retrieving, updating, deleting, and marking tasks
as complete or incomplete. It also includes functionality for
priorities, tags, search, filter, sort, recurrence, and reminder operations.
"""

from datetime import datetime
from typing import Dict, List, Optional
from todo_app.models.task import Task
from todo_app.utils.validators import validate_title, validate_description, validate_task_id, validate_priority, validate_tags, validate_due_date
from todo_app.services.datetime_utils import validate_datetime_format, calculate_next_occurrence, calculate_next_date


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

    def add_task(self, title: str, description: str = "", priority: str = "medium", tags: List[str] = None, due_date: Optional[str] = None,
                 recurrence: Optional[str] = None, due_datetime: Optional[str] = None, **kwargs) -> int:
        """
        Add a new task to the todo list.

        Args:
            title (str): The title of the task (required)
            description (str): The description of the task (optional, default is empty string)
            priority (str): Priority level ('high', 'medium', 'low', default: 'medium')
            tags (List[str]): List of tags for the task (optional, default: [])
            due_date (Optional[str]): Due date in ISO format (YYYY-MM-DD) or None (optional, default: None)
            recurrence (Optional[str]): Recurrence pattern ('daily', 'weekly', 'monthly', or None, default: None)
            due_datetime (Optional[str]): Due date and time in ISO format (YYYY-MM-DD HH:MM) or None (optional, default: None)
            **kwargs: Additional fields for future extensibility

        Returns:
            int: The ID of the newly created task

        Raises:
            ValueError: If any of the inputs are invalid
        """
        # Validate inputs
        validate_title(title)
        validate_description(description)
        validate_priority(priority)
        if tags is None:
            tags = []
        validate_tags(tags)
        validate_due_date(due_date)

        # Validate recurrence pattern
        if recurrence is not None:
            if recurrence not in ["daily", "weekly", "monthly"]:
                raise ValueError(f"Recurrence must be one of 'daily', 'weekly', 'monthly', or None, got: {recurrence}")

        # Validate due_datetime format
        if due_datetime is not None:
            validate_datetime_format(due_datetime)

        # Create a new task with the next available ID
        task_id = self._next_id
        self._next_id += 1

        task = Task(
            id=task_id,
            title=title,
            description=description,
            completed=False,
            priority=priority,
            tags=tags,
            due_date=due_date,
            recurrence=recurrence,
            due_datetime=due_datetime
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

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None,
                   priority: Optional[str] = None, tags: Optional[List[str]] = None,
                   due_date: Optional[str] = None, recurrence: Optional[str] = None,
                   due_datetime: Optional[str] = None, completed: Optional[bool] = None, **kwargs) -> bool:
        """
        Update an existing task.

        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): New title (if provided)
            description (Optional[str]): New description (if provided)
            priority (Optional[str]): New priority (if provided)
            tags (Optional[List[str]]): New list of tags (if provided)
            due_date (Optional[str]): New due date (if provided)
            recurrence (Optional[str]): New recurrence pattern (if provided)
            due_datetime (Optional[str]): New due datetime (if provided)
            completed (Optional[bool]): New completion status (if provided)
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

        if priority is not None:
            validate_priority(priority)
            task.priority = priority

        if tags is not None:
            validate_tags(tags)
            task.tags = tags

        if due_date is not None:
            validate_due_date(due_date)
            task.due_date = due_date

        if recurrence is not None:
            if recurrence not in ["daily", "weekly", "monthly", None]:
                raise ValueError(f"Recurrence must be one of 'daily', 'weekly', 'monthly', or None, got: {recurrence}")
            task.recurrence = recurrence

        if due_datetime is not None:
            validate_datetime_format(due_datetime)
            task.due_datetime = due_datetime

        if completed is not None:
            if not isinstance(completed, bool):
                raise ValueError(f"Completed status must be a boolean, got: {type(completed)}")
            task.completed = completed

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

    def set_priority(self, task_id: int, priority: str) -> bool:
        """
        Set the priority of a task.

        Args:
            task_id (int): The ID of the task to update
            priority (str): The new priority ('high', 'medium', or 'low')

        Returns:
            bool: True if the priority was successfully updated, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist or if the priority is invalid
        """
        validated_id = validate_task_id(task_id)
        validate_priority(priority)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        task = self._tasks[validated_id]
        task.priority = priority
        return True

    def set_tags(self, task_id: int, tags: List[str]) -> bool:
        """
        Set the tags of a task.

        Args:
            task_id (int): The ID of the task to update
            tags (List[str]): The new list of tags

        Returns:
            bool: True if the tags were successfully updated, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist or if the tags are invalid
        """
        validated_id = validate_task_id(task_id)
        validate_tags(tags)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        task = self._tasks[validated_id]
        task.tags = tags
        return True

    def add_tag(self, task_id: int, tag: str) -> bool:
        """
        Add a tag to a task.

        Args:
            task_id (int): The ID of the task to update
            tag (str): The tag to add

        Returns:
            bool: True if the tag was successfully added, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist or if the tag is invalid
        """
        validated_id = validate_task_id(task_id)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        if not isinstance(tag, str):
            raise ValueError(f"Tag must be a string, got: {type(tag)}")

        task = self._tasks[validated_id]
        if tag not in task.tags:
            task.tags.append(tag)
        return True

    def remove_tag(self, task_id: int, tag: str) -> bool:
        """
        Remove a tag from a task.

        Args:
            task_id (int): The ID of the task to update
            tag (str): The tag to remove

        Returns:
            bool: True if the tag was successfully removed, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist or if the tag is invalid
        """
        validated_id = validate_task_id(task_id)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        if not isinstance(tag, str):
            raise ValueError(f"Tag must be a string, got: {type(tag)}")

        task = self._tasks[validated_id]
        if tag in task.tags:
            task.tags.remove(tag)
        return True

    def search_tasks(self, keyword: str) -> List[Task]:
        """
        Search tasks by keyword in title and description.

        Args:
            keyword (str): The keyword to search for (case-insensitive)

        Returns:
            List[Task]: A list of tasks that match the search criteria
        """
        if not isinstance(keyword, str):
            raise ValueError("Search keyword must be a string")

        keyword_lower = keyword.lower()
        matching_tasks = []

        for task in self._tasks.values():
            # Check if keyword appears in title or description (case-insensitive)
            if (keyword_lower in task.title.lower() or
                keyword_lower in task.description.lower()):
                matching_tasks.append(task)

        return matching_tasks

    def filter_tasks(self, status: Optional[str] = None, priority: Optional[str] = None, due_date: Optional[str] = None) -> List[Task]:
        """
        Filter tasks by status, priority, or due date.

        Args:
            status (Optional[str]): Filter by status ('completed' or 'incomplete', default: None)
            priority (Optional[str]): Filter by priority ('high', 'medium', 'low', default: None)
            due_date (Optional[str]): Filter by due date (in ISO format YYYY-MM-DD, default: None)

        Returns:
            List[Task]: A list of tasks that match the filter criteria
        """
        filtered_tasks = []

        for task in self._tasks.values():
            # Check status filter
            if status is not None:
                if status == 'completed' and not task.completed:
                    continue
                elif status == 'incomplete' and task.completed:
                    continue
                elif status not in ['completed', 'incomplete']:
                    raise ValueError(f"Status must be 'completed' or 'incomplete', got: {status}")

            # Check priority filter
            if priority is not None:
                validate_priority(priority)
                if task.priority != priority:
                    continue

            # Check due date filter
            if due_date is not None:
                validate_due_date(due_date)
                if task.due_date != due_date:
                    continue

            filtered_tasks.append(task)

        return filtered_tasks

    def sort_tasks(self, by: str = 'priority') -> List[Task]:
        """
        Sort tasks by priority, due date, or title.

        Args:
            by (str): Sort by 'priority', 'due_date', or 'title' (default: 'priority')

        Returns:
            List[Task]: A list of tasks sorted by the specified criteria
        """
        if by not in ['priority', 'due_date', 'title']:
            raise ValueError(f"Sort by must be 'priority', 'due_date', or 'title', got: {by}")

        tasks_list = list(self._tasks.values())

        if by == 'priority':
            # Map priority to numeric value for sorting: high=1, medium=2, low=3
            priority_map = {'high': 1, 'medium': 2, 'low': 3}
            tasks_list.sort(key=lambda x: (priority_map[x.priority], x.id))
        elif by == 'due_date':
            # Sort by due date, with None values at the end
            tasks_list.sort(key=lambda x: (x.due_date is None, x.due_date, x.id))
        elif by == 'title':
            # Sort alphabetically by title
            tasks_list.sort(key=lambda x: x.title.lower())

        return tasks_list

    def set_recurrence(self, task_id: int, recurrence: str) -> bool:
        """
        Set the recurrence pattern of a task.

        Args:
            task_id (int): The ID of the task to update
            recurrence (str): The recurrence pattern ('daily', 'weekly', 'monthly')

        Returns:
            bool: True if the recurrence was successfully updated, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist or if the recurrence pattern is invalid
        """
        validated_id = validate_task_id(task_id)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        if recurrence not in ["daily", "weekly", "monthly"]:
            raise ValueError(f"Recurrence must be one of 'daily', 'weekly', 'monthly', got: {recurrence}")

        task = self._tasks[validated_id]
        task.recurrence = recurrence
        return True

    def set_due_datetime(self, task_id: int, due_datetime: str) -> bool:
        """
        Set the due datetime of a task.

        Args:
            task_id (int): The ID of the task to update
            due_datetime (str): The due datetime in ISO format (YYYY-MM-DD HH:MM)

        Returns:
            bool: True if the due datetime was successfully updated, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist or if the due datetime is invalid
        """
        validated_id = validate_task_id(task_id)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        validate_datetime_format(due_datetime)

        task = self._tasks[validated_id]
        task.due_datetime = due_datetime
        return True

    def _calculate_next_due(self, current_due: str, pattern: str) -> str:
        """
        Calculate the next due date based on the recurrence pattern.

        Args:
            current_due (str): The current due date/datetime string
            pattern (str): The recurrence pattern ('daily', 'weekly', 'monthly')

        Returns:
            str: The next due date/datetime string
        """
        if current_due is None:
            return None

        # If the current due has time information (contains space), use datetime calculation
        if ' ' in current_due:
            return calculate_next_occurrence(current_due, pattern)
        else:
            # Otherwise, it's just a date, use date calculation
            return calculate_next_date(current_due, pattern)

    def handle_completion(self, task_id: int) -> bool:
        """
        Handle task completion, including creating a new instance for recurring tasks.

        Args:
            task_id (int): The ID of the task to mark as complete

        Returns:
            bool: True if the task was successfully handled, False otherwise

        Raises:
            ValueError: If the task ID doesn't exist
        """
        validated_id = validate_task_id(task_id)

        if validated_id not in self._tasks:
            raise ValueError(f"Task with ID {validated_id} does not exist")

        task = self._tasks[validated_id]

        # Mark the current task as complete
        task.completed = True

        # If the task is recurring, create a new instance with the next occurrence
        if task.recurrence:
            # Calculate the next due date based on the recurrence pattern
            next_due_date = None
            next_due_datetime = None

            if task.due_date:
                next_due_date = self._calculate_next_due(task.due_date, task.recurrence)

            if task.due_datetime:
                next_due_datetime = self._calculate_next_due(task.due_datetime, task.recurrence)

            # Create a new task with the same properties but a new ID and reset completion status
            new_task_id = self._next_id
            self._next_id += 1

            new_task = Task(
                id=new_task_id,
                title=task.title,
                description=task.description,
                completed=False,  # New task starts as incomplete
                priority=task.priority,
                tags=task.tags.copy(),  # Copy the tags list
                due_date=next_due_date,
                recurrence=task.recurrence,
                due_datetime=next_due_datetime
            )

            # Add the new task to storage
            self._tasks[new_task_id] = new_task

        return True

    def check_reminders(self) -> dict:
        """
        Check for overdue and upcoming tasks.

        Returns:
            dict: Dictionary containing lists of overdue and upcoming tasks
        """
        from todo_app.services.datetime_utils import is_overdue, is_upcoming

        overdue_tasks = []
        upcoming_tasks = []

        for task in self._tasks.values():
            # Check for overdue tasks
            if task.due_datetime and is_overdue(task.due_datetime):
                overdue_tasks.append(task)

            # Check for upcoming tasks (due within 24 hours)
            if task.due_datetime and is_upcoming(task.due_datetime, hours_ahead=24):
                upcoming_tasks.append(task)

        return {
            "overdue": overdue_tasks,
            "upcoming": upcoming_tasks
        }

    def get_task_count(self) -> int:
        """
        Get the total number of tasks.

        Returns:
            int: The number of tasks in the system
        """
        return len(self._tasks)