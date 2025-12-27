# Implementation Tasks: Enhanced In-Memory Python Console Todo App with Intermediate Organization & Usability Features

## Feature Overview
Extend the existing basic Todo app to add intermediate organization features: priorities (high/medium/low), tags (multiple labels per task), search by keyword in title/description, filter by status/priority/date, and sort by priority/date/title. Maintain backward compatibility with all existing basic operations while implementing these new features using pure Python standard library with in-memory storage.

**Feature Branch**: `002-todo-app-organization`
**Target**: Python 3.13+ with standard library only, console application

## Dependencies
- User Story 1 (P1) must be completed before User Stories 2, 3, and 4
- User Story 3 (P3) depends on User Story 1 (P1) for priority filtering
- User Story 4 (P3) depends on User Story 1 (P1) for priority sorting

## Parallel Execution Examples
- User Story 2 (Search) and User Story 3 (Filter) can be developed in parallel after User Story 1 is complete
- User Story 4 (Sort) can be developed in parallel with User Story 2 (Search) and User Story 3 (Filter) after User Story 1 is complete

## Implementation Strategy
- MVP: Implement User Story 1 (Add Priority and Tags to Tasks) as a complete, independently testable feature
- Incremental delivery: Each user story builds upon the previous one while maintaining backward compatibility
- Follow the 8-phase implementation process: Update data model → Implement priorities & tags → Add search functionality → Implement filter → Implement sort → Extend menu & display → Full integration test → Polish output formatting

---

## Phase 1: Setup (Project Initialization)

- [X] T001 Create src/models directory structure
- [X] T002 Create src/services directory structure
- [X] T003 Create src/cli directory structure
- [X] T004 Initialize src/models/__init__.py
- [X] T005 Initialize src/services/__init__.py
- [X] T006 Initialize src/cli/__init__.py

---

## Phase 2: Foundational (Blocking Prerequisites)

- [X] T007 Extend Task class with priority, tags, and due_date fields in src/models/task.py
- [X] T008 Implement Task class validation methods in src/models/task.py
- [X] T009 Update existing TodoManager to work with extended Task model in src/services/todo_manager.py

---

## Phase 3: User Story 1 - Add Priority and Tags to Tasks (Priority: P1)

**Goal**: As a user, I want to assign priorities (high/medium/low) and tags (work/home/personal) to my tasks so that I can better organize and identify important tasks. I should be able to add these attributes when creating a new task or update them for existing tasks.

**Independent Test**: Can be fully tested by creating tasks with priorities and tags, updating existing tasks with priorities and tags, and viewing tasks with their priority and tag indicators displayed in the list.

- [X] T010 [US1] Create Task dataclass with priority (str, default 'medium'), tags (list[str], default []), and due_date (str|None, default None) in src/models/task.py
- [X] T011 [US1] Add validation for priority field ('high', 'medium', 'low') in src/models/task.py
- [X] T012 [US1] Add validation for tags field (list of strings) in src/models/task.py
- [X] T013 [US1] Add validation for due_date field (ISO format or None) in src/models/task.py
- [X] T014 [US1] Update TodoManager to support creating tasks with priority and tags in src/services/todo_manager.py
- [X] T015 [US1] Implement set_priority method in TodoManager in src/services/todo_manager.py
- [X] T016 [US1] Implement set_tags method in TodoManager in src/services/todo_manager.py
- [X] T017 [US1] Implement add_tag method in TodoManager in src/services/todo_manager.py
- [X] T018 [US1] Implement remove_tag method in TodoManager in src/services/todo_manager.py
- [X] T019 [US1] Update CLI menu to include options for setting priority and tags in src/cli/menu.py
- [X] T020 [US1] Implement priority setting functionality in CLI interface in src/cli/menu.py
- [X] T021 [US1] Implement tags management functionality in CLI interface in src/cli/menu.py
- [X] T022 [US1] Update task display to show priority indicators [H], [M], [L] in src/cli/menu.py
- [X] T023 [US1] Update task display to show comma-separated tags in src/cli/menu.py
- [X] T024 [US1] Test creating tasks with priority and tags
- [X] T025 [US1] Test updating existing tasks with priority and tags
- [X] T026 [US1] Verify priority and tags display correctly in task list

---

## Phase 4: User Story 2 - Search Tasks by Keyword (Priority: P2)

**Goal**: As a user, I want to search for tasks by keywords in the title or description so that I can quickly find specific tasks among many. The search should be case-insensitive and return all matching tasks.

**Independent Test**: Can be fully tested by creating multiple tasks with different titles and descriptions, then searching for specific keywords and verifying that only matching tasks are returned.

- [X] T027 [US2] Implement search method in TodoManager that searches title and description (case-insensitive) in src/services/todo_manager.py
- [X] T028 [US2] Add search functionality to CLI menu in src/cli/menu.py
- [X] T029 [US2] Implement search input handling in CLI interface in src/cli/menu.py
- [X] T030 [US2] Handle empty search results with appropriate messaging in src/cli/menu.py
- [X] T031 [US2] Test searching by keyword in title
- [X] T032 [US2] Test searching by keyword in description
- [X] T033 [US2] Test case-insensitive search functionality
- [X] T034 [US2] Test empty search results handling

---

## Phase 5: User Story 3 - Filter Tasks by Status, Priority, or Date (Priority: P3)

**Goal**: As a user, I want to filter my task list by status (completed/incomplete), priority (high/medium/low), or date so that I can focus on specific subsets of tasks relevant to my current needs.

**Independent Test**: Can be fully tested by creating tasks with different statuses, priorities, and dates, then applying various filters and verifying that only tasks matching the filter criteria are displayed.

- [X] T035 [US3] Implement filter method in TodoManager for status, priority, and date in src/services/todo_manager.py
- [X] T036 [US3] Add filter functionality to CLI menu in src/cli/menu.py
- [X] T037 [US3] Implement filter selection interface in CLI in src/cli/menu.py
- [X] T038 [US3] Implement status filtering (completed/incomplete) in CLI in src/cli/menu.py
- [X] T039 [US3] Implement priority filtering (high/medium/low) in CLI in src/cli/menu.py
- [X] T040 [US3] Implement date filtering in CLI in src/cli/menu.py
- [X] T041 [US3] Test filtering by status
- [X] T042 [US3] Test filtering by priority
- [X] T043 [US3] Test filtering by date
- [X] T044 [US3] Test filter validation for invalid criteria

---

## Phase 6: User Story 4 - Sort Tasks by Priority, Date, or Alphabetically (Priority: P3)

**Goal**: As a user, I want to sort my tasks by priority, due date, or alphabetically by title so that I can organize them in a way that makes sense for my current workflow.

**Independent Test**: Can be fully tested by creating tasks with different priorities, dates, and titles, then applying various sorting options and verifying that tasks are displayed in the correct order.

- [X] T045 [US4] Implement priority to numeric mapping (high=1, medium=2, low=3) in src/services/todo_manager.py
- [X] T046 [US4] Implement sort method in TodoManager for priority, date, and title in src/services/todo_manager.py
- [X] T047 [US4] Add sort functionality to CLI menu in src/cli/menu.py
- [X] T048 [US4] Implement sort selection interface in CLI in src/cli/menu.py
- [X] T049 [US4] Implement priority sorting in CLI in src/cli/menu.py
- [X] T050 [US4] Implement date sorting in CLI in src/cli/menu.py
- [X] T051 [US4] Implement title alphabetical sorting in CLI in src/cli/menu.py
- [X] T052 [US4] Test sorting by priority (high to low)
- [X] T053 [US4] Test sorting by date (chronological)
- [X] T054 [US4] Test sorting alphabetically by title
- [X] T055 [US4] Test default sort order (priority then ID)

---

## Phase 7: Polish & Cross-Cutting Concerns

- [X] T056 Update main.py to integrate all new features
- [X] T057 Enhance error handling for invalid inputs in CLI interface in src/cli/menu.py
- [X] T058 Implement graceful handling of edge cases (empty searches, invalid filters) in src/cli/menu.py
- [X] T059 Add input validation for priority choices in src/cli/menu.py
- [X] T060 Add input validation for tag inputs in src/cli/menu.py
- [X] T061 Update display formatting for better readability in src/cli/menu.py
- [X] T062 Ensure all basic functionality (add, delete, update, mark complete) continues to work without regression
- [X] T063 Test full integration of all features together
- [X] T064 Perform comprehensive testing of all user stories
- [X] T065 Verify success criteria are met (95% success rate for priorities/tags, search performance, etc.)
- [X] T066 Update documentation to reflect new features
- [X] T067 Final testing and bug fixes