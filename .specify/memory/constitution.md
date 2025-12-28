<!--
Sync Impact Report:
- Version change: 1.0.3 → 1.0.4
- Modified principles: None
- Added sections: Overall Polish in Success Criteria
- Removed sections: None
- Templates requiring updates: ✅ Updated
- Follow-up TODOs: None
-->
# Hackathon II - Evolution of Todo Constitution

## Core Principles

### I. Spec-Driven Development
All new features and modifications must originate from refined specifications using Claude Code; no manual code writing allowed throughout the project. All implementations must be generated through specifications and refined iteratively until Claude Code produces accurate, functional output.

### II. Iterative Refinement
Specifications must be iteratively improved until Claude Code generates accurate, functional output that integrates seamlessly with existing basic and intermediate level code. Continuously refine and enhance specifications to ensure the generated code meets all requirements and quality standards while maintaining backward compatibility.

### III. Backward Compatibility
Do not change or disturb any previous work of basic and intermediate levels; only update existing structures or add new components to preserve all prior functionalities without regressions. All new features must integrate seamlessly with existing functionality without causing regressions or breaking changes to the basic and intermediate todo operations.

### IV. Intelligent Enhancement
Implement advanced features to make the app feel truly smart while maintaining console-based interaction. Design features that provide intelligent behavior and enhanced user experience while staying within the console application paradigm.

### V. Modularity and Extensibility
Extend existing classes cleanly to support recurring tasks and due dates, preparing for future AI/web phases. Code must be structured in a way that allows for easy extension and adaptation to new requirements and platforms while maintaining clean separation of concerns.

### VI. Reusable Intelligence
Strengthen patterns for subagents and agent skills to maximize bonus points. Design systems that can leverage AI capabilities and reusable components to enhance functionality and provide extensibility for future development.

## Key Standards

Code Quality: Maintain PEP8 compliance, add docstrings, type hints, comments for new recurring/due-date logic. All code must follow Python best practices and maintain high readability standards with proper documentation.

Error Handling: Robust validation for recurrence patterns (e.g., daily/weekly), date/time inputs, graceful handling of past-due or invalid recurrences. All user inputs must be validated and appropriate error messages provided for invalid operations, especially for new advanced features.

Menu Integration: Extend main menu with intuitive options for setting recurrence, setting due date/time, viewing upcoming reminders. The user interface must remain intuitive and well-organized as new features are added, with clear menu options for all functionality.

Feature Completeness: Fully implement Advanced Level features:
1. Recurring Tasks - support patterns like daily, weekly, monthly; auto-reschedule completed recurring tasks by creating new instance with next occurrence
2. Due Dates & Time Reminders - allow setting due date/time on tasks; simulate reminders by highlighting overdue/upcoming tasks in list view and console messages (note: browser notifications not possible in pure console, so use console-based alerts/highlights)

All specified features must be fully functional and tested.

Documentation: Update specs history, CLAUDE.md with all new prompts/iterations, README.md if needed. All development artifacts must be properly documented for future reference with clear iteration trails.

## Constraints

Technology Stack: Pure Python 3.13+ with UV; no external dependencies beyond standard library (cannot use browser notifications, so adapt reminders to console output). The project must work within these technology constraints without adding external packages.

Storage: Continue in-memory only; extend Task model with recurrence(str or dict e.g., 'weekly'), due_datetime(str or None). All data must be stored in memory during application runtime with no permanent storage mechanism.

No Manual Edits: All code changes generated solely by Claude Code through spec refinement; do not alter existing basic/intermediate code unless necessary for clean extension. No hand-written code is allowed in the final implementation.

Repository: Keep same structure; add new spec files in specs/features/advanced/ or similar. The project must maintain the specified directory and file structure for proper organization.

Development: WSL2 on Windows; spec-driven process only. The development workflow must be compatible with WSL 2 environment on Windows.

Not Building: Browser-based notifications (replace with console highlights/messages), Web interfaces, AI chatbot, persistence, or deployment (reserved for later phases). These features are explicitly out of scope for the advanced level implementation.

## Success Criteria

Functional Demo: Console app demonstrates all basic+intermediate+advanced features seamlessly; user can create recurring tasks that auto-generate next occurrence on completion, set due dates/times, see highlighted overdue/upcoming tasks with console reminders. The application must be fully functional and demonstrate all required features in an interactive console environment.

Process Verification: Detailed iteration trail in specs-history and CLAUDE.md for advanced additions. The development process must be fully traceable through specifications and history with clear documentation of all iterations.

Integration Quality: Zero regressions in basic/intermediate features; advanced features feel natural and intelligent. All new functionality must integrate seamlessly with existing features without causing any issues.

Extensibility Check: Task model and manager ready for future phases without major rework. The architecture must be modular and extensible to support future enhancements.

Bonus Readiness: Strong reusable intelligence patterns in recurrence/reminder logic. The codebase must include reusable components and patterns that support AI integration and intelligent features.

Overall Polish: Clear menu options, formatted output with due/overdue indicators, recurrence symbols, helpful reminder messages on list view/startup. The application must present a professional, polished user experience with intuitive interactions and clear visual indicators.

## Governance

This constitution governs all development activities for the Hackathon II Todo App project. All implementation must comply with the stated principles and constraints. Amendments to this constitution require explicit documentation and approval. All code generation and development activities must adhere to the Spec-Driven Development principle and no manual coding constraint.

**Version**: 1.0.4 | **Ratified**: 2025-12-27 | **Last Amended**: 2025-12-27
