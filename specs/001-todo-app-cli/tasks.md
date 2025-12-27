# Implementation Tasks: In-Memory Python Console Todo App

## Feature Overview
Implementation of a console-based todo application with in-memory storage that supports the 5 basic features: Add task with title/description, View list with status, Update details, Delete by ID, and Mark Complete/Incomplete. The application follows a modular architecture with clear separation of concerns and is designed for extensibility to support future feature additions.

## Implementation Strategy
- Follow iterative spec-driven development process: specs → generate code with Claude Code → test → refine spec if needed → log in CLAUDE.md
- Build MVP with core functionality first (User Story 1: Add Tasks)
- Incrementally add features following priority order (P1, P2, etc.)
- Each user story should be independently testable
- Follow modular architecture with clear separation of concerns (Task class, TodoManager for logic, CLI for interface)
- Design for extensibility: TodoManager methods should allow future additions (like priority, due_date) without breaking changes

## Dependencies
- User Story 6 (Interactive Menu Navigation) must be partially complete before other stories can be fully tested
- User Story 1 (Add Tasks) provides foundational data for other stories
- Foundational components (Task model, TodoManager) must be complete before user story implementations

## Parallel Execution Examples
- Task model and validator utilities can be developed in parallel
- CLI menu and service layer can be developed in parallel once contracts are established
- Individual user story features can be developed in parallel after foundational components exist

---

## Phase 1: Setup repo

- [x] T001 Create project structure in src/ directory per implementation plan
- [x] T002 Create empty requirements.txt file (no external dependencies)
- [x] T003 Create main.py entry point file
- [x] T004 Create package __init__.py files in todo_app/, models/, services/, cli/, utils/ directories
- [x] T005 Set up basic project configuration files (created .gitignore)

## Phase 2: Define data model

- [x] T006 [P] Create Task dataclass in src/todo_app/models/task.py with id, title, description, completed fields
- [x] T007 [P] Create input validation utilities in src/todo_app/utils/validators.py for title/description length and content
- [x] T008 [P] Design TodoManager service class in src/todo_app/services/todo_manager.py with extensible architecture
- [x] T009 [P] Create basic CLI menu structure in src/todo_app/cli/menu.py with placeholder methods
- [x] T010 Implement ID generation logic in TodoManager (auto-increment)

## Phase 3: Implement core CRUD

- [x] T011 [P] [US1] Implement add_task method in TodoManager with validation for title/description, accepting **kwargs for extensibility
- [x] T012 [P] [US2] Implement get_all_tasks method in TodoManager
- [x] T013 [P] [US2] Implement get_task_by_id method in TodoManager
- [x] T014 [P] [US3] Implement mark_complete method in TodoManager with extensible parameters
- [x] T015 [P] [US3] Implement mark_incomplete method in TodoManager with extensible parameters
- [x] T016 [P] [US4] Implement update_task method in TodoManager with **kwargs for future fields
- [x] T017 [P] [US5] Implement delete_task method in TodoManager
- [x] T018 Add error handling for invalid inputs across all TodoManager methods
- [x] T019 Verify unique ID assignment and data integrity in storage operations

## Phase 4: Build CLI menu

- [x] T020 [US6] Implement main menu loop in CLI with numbered options
- [x] T021 [US6] Create menu option display with clear choices (Add, View, Update, Delete, Mark Complete, Mark Incomplete, Exit)
- [x] T022 [US6] Implement menu navigation logic to return to main menu after operations
- [x] T023 [US6] Add error handling for invalid menu choices
- [x] T024 [US1] Create add task functionality in CLI menu with user prompts
- [x] T025 [US2] Create view all tasks functionality in CLI menu
- [x] T026 [US3] Create mark complete functionality in CLI menu with task ID input
- [x] T027 [US3] Create mark incomplete functionality in CLI menu with task ID input
- [x] T028 [US4] Create update task functionality in CLI menu with task ID and new details input
- [x] T029 [US5] Create delete task functionality in CLI menu with task ID input
- [x] T030 Test menu navigation between different operations

## Phase 5: Polish and test

- [x] T031 [US1] Test adding tasks with valid title and description
- [x] T032 [US1] Test adding tasks with only title (empty description)
- [x] T033 [US1] Test error handling for invalid inputs (empty title, too long inputs)
- [x] T034 [US1] Verify unique ID assignment for each new task
- [x] T035 [US2] Format task display with ID, title, description, and status
- [x] T036 [US2] Handle empty task list case with appropriate message
- [x] T037 [US2] Test viewing tasks after adding them
- [x] T038 [US2] Test viewing empty task list scenario
- [x] T039 [US3] Test marking tasks from incomplete to complete
- [x] T040 [US3] Test marking tasks from complete to incomplete
- [x] T041 [US3] Test error handling for non-existent task IDs
- [x] T042 [US4] Test updating task title and description
- [x] T043 [US4] Test error handling for non-existent task IDs during update
- [x] T044 [US4] Test validation for invalid updated inputs
- [x] T045 [US5] Test deleting existing tasks
- [x] T046 [US5] Test error handling for non-existent task IDs during deletion
- [x] T047 [US5] Verify task no longer appears in list after deletion
- [x] T048 Implement comprehensive input validation across all user inputs
- [x] T049 Add user-friendly error messages with clear guidance for all validation failures
- [x] T050 Handle special characters in task titles and descriptions appropriately
- [x] T051 Test all edge cases identified in specification (invalid IDs, empty lists, etc.)
- [x] T052 Ensure system state remains unchanged after validation errors
- [x] T053 Add sanitization to prevent injection attacks in input fields
- [x] T054 Integrate all components in main.py with proper error handling
- [x] T055 Add docstrings and type hints to all functions and classes
- [x] T056 Perform end-to-end testing of all 5 basic operations
- [x] T057 Test error handling for invalid inputs and ID not found scenarios
- [x] T058 Verify application meets all success criteria from specification
- [x] T059 Optimize performance to ensure response times < 1 second
- [x] T060 Create README.md with setup and usage instructions
- [x] T061 Validate code follows PEP8 standards and includes meaningful variable names
- [x] T062 Verify extensibility design allows for future field additions without breaking changes