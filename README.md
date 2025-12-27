# In-Memory Python Console Todo App

A simple, interactive command-line todo application built with Python. This application allows users to manage tasks with a full set of CRUD operations through an intuitive menu system.

## Features

- Add new tasks with title and optional description
- View all tasks with their completion status
- Update existing tasks
- Delete tasks by ID
- Mark tasks as complete/incomplete
- Interactive menu navigation
- Input validation and error handling

## Requirements

- Python 3.13+ (no external dependencies required)

## Setup and Installation

1. Clone or download the repository
2. Navigate to the project directory
3. Run the application using Python:

```bash
python src/main.py
```

## Usage

The application provides a menu-driven interface with the following options:

1. **Add new task** - Create a new task with a title and optional description
2. **View all tasks** - Display all tasks with their status (✓ for complete, ○ for incomplete)
3. **Update task** - Modify an existing task's title and/or description
4. **Delete task** - Remove a task by its ID
5. **Mark task as complete** - Change a task's status to complete
6. **Mark task as incomplete** - Change a task's status to incomplete
7. **Exit** - Quit the application

## Architecture

The application follows a modular architecture:

- `main.py` - Application entry point
- `src/todo_app/cli/menu.py` - Interactive menu interface
- `src/todo_app/services/todo_manager.py` - Core business logic
- `src/todo_app/models/task.py` - Task data model
- `src/todo_app/utils/validators.py` - Input validation utilities

## Design Principles

- **In-memory storage**: Tasks are stored in memory during the session (no persistence)
- **Extensible design**: Architecture allows for future feature additions
- **Input validation**: Comprehensive validation for all user inputs
- **Error handling**: Graceful handling of invalid inputs and edge cases
- **User-friendly**: Clear messages and intuitive navigation

## Testing

All functionality has been thoroughly tested with the included test suite:

```bash
python test_functionality.py
```

## Success Criteria

The application successfully implements all 5 basic features:
1. Add task with title/description
2. View list with status
3. Update details
4. Delete by ID
5. Mark complete/incomplete

The application is designed for extensibility and follows clean code principles.