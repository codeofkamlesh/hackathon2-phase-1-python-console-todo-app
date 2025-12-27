# Quickstart Guide: In-Memory Python Console Todo App

## Prerequisites

- Python 3.13+ installed
- WSL2 (if on Windows)
- No external dependencies required

## Setup

1. Clone the repository
2. Navigate to the project directory
3. Ensure Python 3.13+ is available in your environment

## Running the Application

```bash
python src/main.py
```

## Basic Usage

1. Launch the application with the command above
2. The main menu will display available options:
   - 1. Add new task
   - 2. View all tasks
   - 3. Update task
   - 4. Delete task
   - 5. Mark task as complete
   - 6. Mark task as incomplete
   - 7. Exit
3. Select an option by entering the corresponding number
4. Follow the prompts to provide required information
5. The application will process your request and return to the main menu

## Example Workflow

1. Select "Add new task" (option 1)
2. Enter a title for the task
3. Optionally enter a description
4. The task will be added with a unique ID
5. Select "View all tasks" (option 2) to see your tasks
6. Use other options to manage your tasks as needed

## Error Handling

- If you enter invalid input, the application will display a user-friendly error message
- Follow the guidance provided to correct your input
- The application will return to the main menu after processing each action or error

## Development Process

The application follows an iterative spec-driven development process:
1. Refine specifications as needed
2. Generate code with Claude Code from specs
3. Test functionality
4. Refine specifications if needed
5. Log all changes in CLAUDE.md

## Architecture

The application is organized with clear separation of concerns:
- Models: Data structures (Task class)
- Services: Business logic (TodoManager class)
- CLI: User interface (Menu class)
- Utils: Helper functions (Validators)

## Extensibility

The architecture is designed to support future feature additions:
- Priority levels
- Due dates
- Tags or categories
- Subtasks or dependencies
- Recurring tasks

New features can be added without breaking existing functionality.

## Development

To modify or extend the application:

1. The main entry point is in `src/main.py`
2. Task model is defined in `src/todo_app/models/task.py`
3. Business logic is in `src/todo_app/services/todo_manager.py`
4. CLI interface is in `src/todo_app/cli/menu.py`
5. Validation utilities are in `src/todo_app/utils/validators.py`