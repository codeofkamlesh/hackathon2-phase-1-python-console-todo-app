# Research: Advanced Todo App Features

## Decision: Recurrence patterns (support 'daily','weekly','monthly' via string)
**Rationale**: Using simple string values for recurrence patterns (daily, weekly, monthly) provides a clear, easy-to-understand interface while allowing for future expansion. Monthly recurrence is approximated as +30 days for simplicity rather than exact calendar month handling.

**Alternatives considered**:
- Integer-based enums: Less readable for console application
- Complex interval objects: More complex than needed for basic recurring patterns
- Natural language parsing: Would require additional dependencies and complexity

## Decision: Due datetime storage (ISO string 'YYYY-MM-DD HH:MM' parsed with datetime.strptime)
**Rationale**: Using ISO format strings for due datetime storage maintains simplicity while being human-readable and easily parseable. This format is standard and allows for accurate date/time comparisons.

**Alternatives considered**:
- Unix timestamps: Less human-readable and harder to debug
- Separate date/time objects: Would complicate serialization in in-memory storage
- Custom format: Would require custom parsing logic

## Decision: Recurring completion behavior (mark complete → create new task with same details but due_datetime shifted by interval)
**Rationale**: When a recurring task is marked complete, creating a new task with the same details but a shifted due date provides a clean approach that maintains the original task's properties while generating the next occurrence.

**Alternatives considered**:
- Modifying the existing task: Would lose completion history
- Flagging as recurring and modifying in place: More complex state management
- Using templates: Would require additional template management system

## Decision: Current time source (use datetime.now() for real-time checks; allow manual override in testing)
**Rationale**: Using datetime.now() for real-time checks is the standard approach for time-sensitive applications. Allowing manual override in testing ensures reliable testing of time-dependent functionality.

**Alternatives considered**:
- System clock access: Less reliable and more complex
- External time services: Unnecessary for console application

## Decision: Reminder thresholds (overdue: any past due, upcoming: within next 24 hours)
**Rationale**: Setting overdue as any past-due task provides immediate visibility for missed deadlines. Setting upcoming as within 24 hours gives users a reasonable window to prepare for upcoming tasks.

**Alternatives considered**:
- Different time windows: 12 hours, 48 hours - 24 hours provides a good balance
- Configurable thresholds: Would add unnecessary complexity for this phase

## Decision: Color output (use ANSI escape codes for red/yellow/green indicators, fallback to symbols if no color support)
**Rationale**: ANSI escape codes provide rich color output for console applications while being widely supported. Fallback to symbols ensures compatibility across different terminal types.

**Alternatives considered**:
- Third-party color libraries: Would violate no-external-dependencies constraint
- HTML formatting: Not applicable to console application

## Implementation Process Decisions

### Process Flow
**Decision**: Follow iterative process of starting from current working code → refining specs → generating full updated implementation → testing each addition → refining specs only on failures → documenting every prompt/output
**Rationale**: This aligns with the spec-driven development principle and allows for continuous improvement based on testing feedback. The iterative approach ensures quality while maintaining compliance with the constitution. Documenting every prompt/output in CLAUDE.md ensures full traceability.

**Alternatives considered**:
- One-pass implementation: Higher risk of missing requirements or introducing bugs

### Implementation Phases
**Decision**: Organize implementation in 9 distinct phases for systematic development
**Rationale**: Breaking down the implementation into manageable phases allows for focused development, easier testing, and better risk management. Each phase builds upon the previous one while maintaining backward compatibility.

**Phase sequence**:
1. Model extensions: Add recurrence and due_datetime fields to Task class
2. Due date/time input & parsing: Implement date/time input handling and validation
3. Recurrence setting & validation: Add recurrence pattern setting and validation
4. Auto-respawn on completion: Implement recurring task auto-creation on completion
5. Reminder detection & alerting: Implement overdue/upcoming task detection and alerts
6. Enhanced colored/symbol display: Add ANSI color and symbol support for visual indicators
7. Menu & interaction updates: Add CLI options for new features and update interactions
8. Full regression + scenario testing: Verify all components work together and test scenarios
9. Final polish & demo preparation: Polish output and prepare for demonstration

**Alternatives considered**:
- All-at-once implementation: Higher complexity and harder to debug
- Parallel development: Risk of integration issues without proper sequencing