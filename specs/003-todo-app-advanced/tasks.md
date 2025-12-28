# Implementation Tasks: Intelligent In-Memory Python Console Todo App with Advanced Features

## Feature Overview
Extend the existing basic + intermediate Todo app to add advanced intelligent features: recurring tasks with daily/weekly/monthly patterns, due date/time reminders with console-based alerts, and enhanced display with ANSI color highlights and symbols. Maintain backward compatibility with all existing basic and intermediate operations while implementing these new features using pure Python standard library with in-memory storage.

**Feature Branch**: `003-todo-app-advanced`
**Target**: Python 3.13+ with standard library only, console application

## Dependencies
- User Story 1 (P1) must be completed before User Stories 2 and 3 can be fully tested
- User Story 2 (P2) can be developed in parallel with User Story 1 (P1) after foundational setup
- User Story 3 (P3) depends on User Stories 1 and 2 for full functionality

## Parallel Execution Examples
- User Story 1 (Recurring Tasks) and User Story 2 (Due Date Reminders) can be developed in parallel after Phase 2 (Foundational) is complete
- Model extensions and datetime utilities can be developed in parallel with service layer updates

## Implementation Strategy
- MVP: Implement User Story 1 (Create Recurring Tasks) as a complete, independently testable feature
- Incremental delivery: Each user story builds upon the previous one while maintaining backward compatibility
- Follow the 9-phase implementation process: Model extensions → Due date/time input & parsing → Recurrence setting & validation → Auto-respawn on completion → Reminder detection & alerting → Enhanced colored/symbol display → Menu & interaction updates → Full regression + scenario testing → Final polish & demo preparation

---

## Phase 1: Setup (Project Initialization)

- [ ] T001 Create src/models directory structure if not exists
- [ ] T002 Create src/services directory structure if not exists
- [ ] T003 Create src/cli directory structure if not exists
- [ ] T004 Initialize src/models/__init__.py
- [ ] T005 Initialize src/services/__init__.py
- [ ] T006 Initialize src/cli/__init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

- [ ] T007 Extend Task class with recurrence, due_datetime, and due_date fields in src/models/task.py
- [ ] T008 Implement Task class validation methods for new fields in src/models/task.py
- [ ] T009 Update existing TodoManager to work with extended Task model in src/services/todo_manager.py
- [ ] T010 Create datetime_utils.py module for parsing/adding intervals in src/services/datetime_utils.py

---

## Phase 3: User Story 1 - Create Recurring Tasks (Priority: P1)

**Goal**: As a user, I want to create tasks that repeat on a schedule (daily, weekly, monthly) so that I don't have to manually recreate routine tasks. When I mark a recurring task as complete, a new instance should automatically be created with the next occurrence date based on the recurrence pattern.

**Independent Test**: Can be fully tested by creating recurring tasks with different patterns (daily, weekly, monthly), marking them as complete, and verifying that new instances are automatically created with the correct next occurrence dates.

- [ ] T011 [US1] Update Task dataclass with recurrence (str|None, default None) and due_datetime (str|None, default None) fields in src/models/task.py
- [ ] T012 [US1] Add validation for recurrence field ('daily', 'weekly', 'monthly', or None) in src/models/task.py
- [ ] T013 [US1] Add validation for due_datetime field (ISO format or None) in src/models/task.py
- [ ] T014 [US1] Update TodoManager to support creating tasks with recurrence and due_datetime in src/services/todo_manager.py
- [ ] T015 [US1] Implement set_recurrence method in TodoManager in src/services/todo_manager.py
- [ ] T016 [US1] Implement set_due_datetime method in TodoManager in src/services/todo_manager.py
- [ ] T017 [US1] Implement _calculate_next_due helper method in TodoManager in src/services/todo_manager.py
- [ ] T018 [US1] Implement handle_completion logic for recurring tasks in TodoManager in src/services/todo_manager.py
- [ ] T019 [US1] Create datetime utility functions for recurrence calculations in src/services/datetime_utils.py
- [ ] T020 [US1] Update CLI menu to include option for setting recurring pattern on task in src/cli/menu.py
- [ ] T021 [US1] Implement recurrence setting functionality in CLI interface in src/cli/menu.py
- [ ] T022 [US1] Update task display to show recurrence symbol [↻] in src/cli/menu.py
- [ ] T023 [US1] Test creating daily recurring tasks
- [ ] T024 [US1] Test creating weekly recurring tasks
- [ ] T025 [US1] Test creating monthly recurring tasks
- [ ] T026 [US1] Test marking recurring tasks as complete and auto-spawning new instances

---

## Phase 4: User Story 2 - Set Due Dates and View Reminders (Priority: P2)

**Goal**: As a user, I want to set due dates and times on tasks and receive console-based reminders so that I can stay on top of important deadlines. The app should highlight overdue tasks and upcoming reminders in the list view and provide console alerts on startup.

**Independent Test**: Can be fully tested by creating tasks with due dates, viewing the list to see overdue/upcoming indicators, and verifying console reminder alerts on startup.

- [ ] T027 [US2] Implement due date/time validation in datetime_utils.py in src/services/datetime_utils.py
- [ ] T028 [US2] Implement check_reminders method in TodoManager in src/services/todo_manager.py
- [ ] T029 [US2] Implement overdue detection logic in TodoManager in src/services/todo_manager.py
- [ ] T030 [US2] Implement upcoming reminder detection (within 24 hours) in TodoManager in src/services/todo_manager.py
- [ ] T031 [US2] Add console reminder alerts on app startup in src/cli/menu.py
- [ ] T032 [US2] Add console reminder alerts before task list view in src/cli/menu.py
- [ ] T033 [US2] Implement ANSI color output for overdue/upcoming indicators in src/cli/menu.py
- [ ] T034 [US2] Update task display to show due date/time indicators [⏰] in src/cli/menu.py
- [ ] T035 [US2] Update task display to show overdue indicators [!!!] in red in src/cli/menu.py
- [ ] T036 [US2] Test setting due dates on tasks
- [ ] T037 [US2] Test overdue task detection and display
- [ ] T038 [US2] Test upcoming reminder detection and alerts

---

## Phase 5: User Story 3 - Manage Recurrence and Due Date Settings (Priority: P3)

**Goal**: As a user, I want intuitive menu options for setting recurrence patterns and due dates/times so that I can easily configure advanced task behaviors without complex input. The interface should be clear and provide appropriate validation.

**Independent Test**: Can be fully tested by accessing the menu options for setting recurrence patterns and due dates, entering various values, and verifying they are properly applied to tasks.

- [ ] T039 [US3] Add "Set recurring pattern on task" option to CLI menu in src/cli/menu.py
- [ ] T040 [US3] Add "Set due date & time on task" option to CLI menu in src/cli/menu.py
- [ ] T041 [US3] Add "View reminders summary" option to CLI menu in src/cli/menu.py
- [ ] T042 [US3] Update "Mark as complete" functionality to trigger auto-respawn if recurring in src/cli/menu.py
- [ ] T043 [US3] Implement recurrence pattern selection interface in CLI in src/cli/menu.py
- [ ] T044 [US3] Implement due date/time input interface in CLI in src/cli/menu.py
- [ ] T045 [US3] Implement strict ISO format validation with helpful error messages in src/cli/menu.py
- [ ] T046 [US3] Handle None values gracefully in CLI input processing in src/cli/menu.py
- [ ] T047 [US3] Test recurrence pattern setting via menu interface
- [ ] T048 [US3] Test due date/time setting via menu interface
- [ ] T049 [US3] Test reminder summary functionality
- [ ] T050 [US3] Test error handling for invalid date formats

---

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T051 Update main.py to integrate all new advanced features
- [ ] T052 Enhance error handling for invalid date/time inputs in CLI interface in src/cli/menu.py
- [ ] T053 Implement graceful handling of edge cases (month-end recurrence shifts) in src/services/todo_manager.py
- [ ] T054 Add input validation for recurrence patterns in src/cli/menu.py
- [ ] T055 Add input validation for due date/time formats in src/cli/menu.py
- [ ] T056 Update display formatting for better readability with ANSI colors in src/cli/menu.py
- [ ] T057 Ensure all basic and intermediate functionality continues to work without regression
- [ ] T058 Test full integration of all advanced features together
- [ ] T059 Perform comprehensive regression testing of all features
- [ ] T060 Verify success criteria are met (95% success rate for recurring tasks, 98% accuracy for reminders, etc.)
- [ ] T061 Update documentation to reflect new advanced features
- [ ] T062 Final testing and bug fixes
- [ ] T063 Prepare demo environment and test scenarios
- [ ] T064 Polish output formatting and user experience