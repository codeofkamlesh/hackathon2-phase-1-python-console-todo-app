# Research: Todo App Organization Features

## Decision: Priority representation (enum vs str with validation)
**Rationale**: Using string validation is simpler and more flexible for this console application. We'll validate against allowed values ('high', 'medium', 'low') with a default of 'medium'. This approach is straightforward to implement with Python's standard library and provides clear user-facing values without requiring additional enum imports.

**Alternatives considered**:
- Python Enum: More structured but adds complexity for a simple three-value field
- Integer mapping: Less user-friendly for console display

## Decision: Tags storage (list[str] vs set[str])
**Rationale**: Using list[str] is preferred to allow duplicate tag handling and maintain insertion order. While sets would prevent duplicates, lists provide more flexibility for tag management operations and are more intuitive for console application users.

**Alternatives considered**:
- set[str]: Prevents duplicate tags but loses insertion order
- tuple[str]: Immutable but doesn't allow dynamic tag addition/removal

## Decision: Due date format (simple str like '2025-12-31' vs None for now)
**Rationale**: Using string format for due dates with None as default maintains simplicity for current phase while allowing for future enhancement. Format will follow ISO 8601 (YYYY-MM-DD) for consistency and simple string comparison for sorting/filtering.

**Alternatives considered**:
- datetime objects: More complex parsing and formatting
- timestamp integers: Less readable for console display

## Decision: Search scope (title+description vs full text)
**Rationale**: Searching both title and description provides comprehensive search capability that users expect while keeping implementation simple. Case-insensitive search will be implemented using Python's lower() method for broad compatibility.

**Alternatives considered**:
- Title only: Less comprehensive search
- Full text including tags: More complex but potentially more useful

## Decision: Filter combinations (single vs multiple criteria)
**Rationale**: Implementing single filter criteria first allows for simpler user interface and easier testing. Multiple criteria can be added in future iterations if needed. This approach maintains consistency with basic console application design.

**Alternatives considered**:
- Multiple criteria: More powerful but more complex UI and logic

## Decision: Sort key priorities (high>medium>low mapping to numbers)
**Rationale**: Using a mapping of high=1, medium=2, low=3 (ascending numeric sort) provides clear priority ordering that aligns with user expectations. This allows for simple numeric comparison during sorting operations.

**Alternatives considered**:
- String-based sorting: Would not produce correct priority order
- Custom comparator: More complex than numeric mapping

## Decision: Display order (default sort by priority then ID)
**Rationale**: Default sorting by priority first (high to low) then by ID (oldest to newest) provides a logical default view that highlights important tasks while maintaining consistent ordering. This approach helps users focus on high-priority items first.

**Alternatives considered**:
- Sort by creation time only: Ignores priority levels
- Sort by due date first: Not applicable since due dates are optional in this phase

## Implementation Process Decisions

### Process Flow
**Decision**: Follow iterative process of refining specs → generating code → testing → refining specs
**Rationale**: This aligns with the spec-driven development principle and allows for continuous improvement based on testing feedback. The iterative approach ensures quality while maintaining compliance with the constitution.

**Alternatives considered**:
- One-pass implementation: Higher risk of missing requirements or introducing bugs

### Implementation Phases
**Decision**: Organize implementation in 8 distinct phases for systematic development
**Rationale**: Breaking down the implementation into manageable phases allows for focused development, easier testing, and better risk management. Each phase builds upon the previous one while maintaining backward compatibility.

**Phase sequence**:
1. Update data model: Extend Task class with new attributes
2. Implement priorities & tags: Core functionality for task organization
3. Add search functionality: Enable keyword-based task discovery
4. Implement filter: Allow subset selection based on criteria
5. Implement sort: Enable ordered task display
6. Extend menu & display: User interface for new features
7. Full integration test: Verify all components work together
8. Polish output formatting: Enhance user experience

**Alternatives considered**:
- All-at-once implementation: Higher complexity and harder to debug
- Parallel development: Risk of integration issues without proper sequencing