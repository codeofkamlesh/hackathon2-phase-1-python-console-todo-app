# Task API Contract: In-Memory Python Console Todo App

## Overview

This contract defines the interface for the Todo application's core functionality. Since this is a console application, these represent the internal method contracts within the application rather than external API endpoints. The design emphasizes extensibility to support future feature additions without breaking changes.

## Task Management Operations

### Add Task
- **Method**: `TodoManager.add_task(title: str, description: str = "", **kwargs) -> int`
- **Input**:
  - title (required, str): Task title (1-200 characters)
  - description (optional, str): Task description (0-1000 characters)
  - **kwargs (optional): Additional fields for future extensions (priority, due_date, etc.)
- **Output**: int (new task ID)
- **Success**: Returns the ID of the newly created task
- **Errors**: Raises ValueError for invalid input

### Get All Tasks
- **Method**: `TodoManager.get_all_tasks() -> List[Task]`
- **Input**: None
- **Output**: List of Task objects
- **Success**: Returns all tasks in the system
- **Errors**: None

### Get Task by ID
- **Method**: `TodoManager.get_task_by_id(task_id: int) -> Task`
- **Input**: task_id (int)
- **Output**: Task object
- **Success**: Returns the requested Task object
- **Errors**: Raises ValueError if task ID doesn't exist

### Update Task
- **Method**: `TodoManager.update_task(task_id: int, title: str = None, description: str = None, **kwargs) -> bool`
- **Input**:
  - task_id (int): ID of task to update
  - title (optional, str): New title (if provided)
  - description (optional, str): New description (if provided)
  - **kwargs (optional): Additional fields for future extensions
- **Output**: bool (success indicator)
- **Success**: Returns True if task was updated
- **Errors**: Raises ValueError if task ID doesn't exist

### Delete Task
- **Method**: `TodoManager.delete_task(task_id: int) -> bool`
- **Input**: task_id (int)
- **Output**: bool (success indicator)
- **Success**: Returns True if task was deleted
- **Errors**: Raises ValueError if task ID doesn't exist

### Mark Task Complete
- **Method**: `TodoManager.mark_complete(task_id: int) -> bool`
- **Input**: task_id (int)
- **Output**: bool (success indicator)
- **Success**: Returns True if task status was updated
- **Errors**: Raises ValueError if task ID doesn't exist

### Mark Task Incomplete
- **Method**: `TodoManager.mark_incomplete(task_id: int) -> bool`
- **Input**: task_id (int)
- **Output**: bool (success indicator)
- **Success**: Returns True if task status was updated
- **Errors**: Raises ValueError if task ID doesn't exist

## Extensibility Considerations

### Future Operations
- `TodoManager.set_priority(task_id: int, priority: str) -> bool`
- `TodoManager.set_due_date(task_id: int, due_date: str) -> bool`
- `TodoManager.add_tag(task_id: int, tag: str) -> bool`

### Design Principles
- Methods accept `**kwargs` to accommodate future parameters without breaking changes
- Task model designed to support additional fields
- Return types and core functionality remain consistent for backward compatibility

## Validation Contract

### Input Validation
- Title: 1-200 characters, not empty or whitespace only
- Description: 0-1000 characters
- Task ID: Positive integer that exists in the system
- All inputs sanitized to prevent injection attacks
- Future fields will have appropriate validation rules

### Error Handling Contract
- All invalid inputs result in user-friendly error messages
- Error messages provide clear guidance on how to correct input
- System state remains unchanged after validation errors