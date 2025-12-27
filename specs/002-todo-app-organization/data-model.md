# Data Model: Todo App Organization Features

## Task Entity

**Description**: Represents a todo item with enhanced organization features

**Fields**:
- `id: int` - Unique identifier for the task (auto-incremented)
- `title: str` - Title of the task (required)
- `description: str` - Detailed description of the task (optional, default: "")
- `completed: bool` - Completion status (default: False)
- `priority: str` - Priority level (default: "medium", values: "high", "medium", "low")
- `tags: list[str]` - List of tags associated with the task (default: [])
- `due_date: str | None` - Due date in ISO format (YYYY-MM-DD) or None (default: None)

**Validation Rules**:
- `priority` must be one of: "high", "medium", "low"
- `tags` must be a list of strings (no validation on tag format for now)
- `due_date` must be in ISO format (YYYY-MM-DD) if provided, or None

**State Transitions**:
- `completed` can transition from False to True (mark complete)
- `completed` can transition from True to False (mark incomplete)
- All other fields can be modified through update operations

## Priority Enum Mapping

**Priority to Numeric Mapping**:
- "high" → 1
- "medium" → 2
- "low" → 3

This mapping allows for proper sorting where high priority tasks appear first.

## Tag Management

**Constraints**:
- Tags are stored as a list to maintain insertion order
- Duplicate tags are allowed (user responsibility to manage)
- Tags can be added or removed individually
- Tags are case-sensitive strings