# Data Model: In-Memory Python Console Todo App

## Task Entity

**Definition**: The core entity representing a todo item in the system

**Fields**:
- `id` (int): Unique identifier for the task, auto-incremented
- `title` (str): Required title of the task, maximum 200 characters
- `description` (str): Optional description of the task, maximum 1000 characters
- `completed` (bool): Status indicating whether the task is completed (default: False)

**Extensibility Considerations**:
- Additional fields can be added in the future (priority, due_date, tags, etc.) without breaking existing functionality
- The dataclass approach allows for default values for new optional fields
- The storage mechanism (dict mapping ID to Task objects) naturally supports additional fields

**Validation Rules**:
- ID must be unique within the system
- Title must not be empty or only whitespace
- Title length must be between 1 and 200 characters
- Description length must be between 0 and 1000 characters
- ID must be a positive integer

**State Transitions**:
- `incomplete` → `complete`: When user marks task as done
- `complete` → `incomplete`: When user marks task as not done

## TaskList/Storage Model

**Definition**: Container for managing multiple Task entities in memory

**Structure**: Dictionary mapping ID (int) to Task objects
- Key: Task ID (integer)
- Value: Task object instance

**Operations**:
- Add new task: Insert task with next available ID
- Retrieve task: Access by ID in O(1) time
- Update task: Modify existing task by ID
- Delete task: Remove task by ID
- List all tasks: Return all tasks in the system

**Constraints**:
- All IDs must be unique
- No persistence outside of application runtime
- Memory usage should remain efficient for up to 1000 tasks

## Task Status

**Definition**: Enumeration of possible states for a Task

**Values**:
- `incomplete` (False): Task has not been completed
- `complete` (True): Task has been completed

**Rules**:
- Only two possible states
- State can be toggled by user action
- State changes are immediate and persistent in memory

## Future Extensions

**Planned Extensibility**:
- Priority levels (e.g., low, medium, high)
- Due dates for tasks
- Tags or categories for tasks
- Subtasks or task dependencies
- Recurring tasks

**Implementation Strategy**:
- New fields will be added as optional with sensible defaults
- Existing methods will continue to work unchanged
- New methods will be added to support extended functionality