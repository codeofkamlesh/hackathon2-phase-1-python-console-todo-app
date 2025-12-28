# Data Model: Advanced Todo App Features

## Task Entity (Extended)

**Description**: Represents a todo item with enhanced organization and advanced features

**Fields**:
- `id: int` - Unique identifier for the task (auto-incremented)
- `title: str` - Title of the task (required)
- `description: str` - Detailed description of the task (optional, default: "")
- `completed: bool` - Completion status (default: False)
- `priority: str` - Priority level (default: "medium", values: "high", "medium", "low")
- `tags: list[str]` - List of tags associated with the task (default: [])
- `due_date: str | None` - Due date in ISO format (YYYY-MM-DD) or None (default: None)
- `recurrence: str | None` - Recurrence pattern (default: None, values: "daily", "weekly", "monthly")
- `due_datetime: str | None` - Due date and time in ISO format (YYYY-MM-DD HH:MM) or None (default: None)

**Validation Rules**:
- `priority` must be one of: "high", "medium", "low"
- `tags` must be a list of strings (no validation on tag format for now)
- `due_date` must be in ISO format (YYYY-MM-DD) if provided, or None
- `recurrence` must be one of: "daily", "weekly", "monthly", or None
- `due_datetime` must be in ISO format (YYYY-MM-DD HH:MM) if provided, or None

**State Transitions**:
- `completed` can transition from False to True (mark complete)
- `completed` can transition from True to False (mark incomplete)
- All other fields can be modified through update operations

## Recurrence Pattern Mapping

**Recurrence to Interval Mapping**:
- "daily" → +1 day
- "weekly" → +7 days
- "monthly" → +30 days (approximation)

This mapping allows for proper calculation of next occurrence dates.

## Task Creation Process for Recurring Tasks

When a recurring task is marked complete:
1. Create a new task with the same properties as the original
2. Calculate the next due date based on the recurrence pattern
3. Assign a new ID to the new task
4. Set the new task's completion status to False
5. Preserve all other properties (title, description, priority, tags, etc.)