"""
TodoManager service for the Todo App.

This module provides the core business logic for managing tasks,
including adding, retrieving, updating, deleting, and marking tasks
as complete or incomplete. It also includes functionality for
priorities, tags, search, filter, and sort operations.
"""

from typing import Dict, List, Optional
from todo_app.models.task import Task
from todo_app.utils.validators import validate_title, validate_description, validate_task_id, validate_priority, validate_tags, validate_due_date


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

    def add_task(self, title: str, description: str = "", priority: str = "medium", tags: List[str] = None, due_date: Optional[str] = None, **kwargs) -> int:
        """
        Add a new task to the todo list.

        Args:
            title (str): The title of the task (required)
            description (str): The description of the task (optional, default is empty string)
            priority (str): Priority level ('high', 'medium', 'low', default: 'medium')
            tags (List[str]): List of tags for the task (optional, default: [])
            due_date (Optional[str]): Due date in ISO format (YYYY-MM-DD) or None (optional, default: None)
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
            due_date=due_date
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
                   due_date: Optional[str] = None, completed: Optional[bool] = None, **kwargs) -> bool:
        """
        Update an existing task.

        Args:
            task_id (int): The ID of the task to update
            title (Optional[str]): New title (if provided)
            description (Optional[str]): New description (if provided)
            priority (Optional[str]): New priority (if provided)
            tags (Optional[List[str]]): New list of tags (if provided)
            due_date (Optional[str]): New due date (if provided)
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

    def get_task_count(self) -> int:
        """
        Get the total number of tasks.

        Returns:
            int: The number of tasks in the system
        """
        return len(self._tasks)