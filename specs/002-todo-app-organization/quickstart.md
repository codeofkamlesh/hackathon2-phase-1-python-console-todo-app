# Quickstart Guide: Todo App Organization Features

## Overview
This guide provides setup and usage instructions for the enhanced todo app with organization features including priorities, tags, search, filter, and sort capabilities.

## Prerequisites
- Python 3.13+
- No external dependencies required (pure standard library)

## Setup
1. Ensure Python 3.13+ is installed
2. Clone or access the project repository
3. Navigate to the project directory
4. Run the application with: `python main.py`

## New Feature Usage

### Setting Task Priority
- When creating a task, specify priority as "high", "medium", or "low"
- When updating a task, change priority to one of the three allowed values
- Priority is displayed as [H], [M], or [L] in task lists

### Adding Tags
- Add multiple tags to tasks separated by commas (e.g., "work,urgent,project")
- Tags are displayed as comma-separated values in task lists
- Update existing tasks to add or modify tags

### Searching Tasks
- Use the search option to find tasks by keyword
- Search looks in both title and description fields
- Search is case-insensitive

### Filtering Tasks
- Filter by completion status (completed/incomplete)
- Filter by priority (high/medium/low)
- Filter by due date (if set)

### Sorting Tasks
- Sort by priority (high to low)
- Sort by due date (chronological)
- Sort alphabetically by title

## Menu Options
The main menu includes new options:
- Assign priority to tasks
- Manage tags for tasks
- Search tasks
- Filter tasks
- Sort tasks

## Testing
Manual console testing is recommended:
1. Create tasks with various priorities and tags
2. Test search functionality with different keywords
3. Apply different filters and verify results
4. Test sorting in different modes
5. Verify all basic functionality still works without regression