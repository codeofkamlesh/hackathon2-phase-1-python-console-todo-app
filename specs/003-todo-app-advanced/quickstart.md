# Quickstart Guide: Advanced Todo App Features

## Overview
This guide provides setup and usage instructions for the enhanced todo app with advanced features including recurring tasks and due date/time reminders.

## Prerequisites
- Python 3.13+
- No external dependencies required (pure standard library)

## Setup
1. Ensure Python 3.13+ is installed
2. Clone or access the project repository
3. Navigate to the project directory
4. Run the application with: `python main.py`

## New Feature Usage

### Creating Recurring Tasks
- When creating or updating a task, select a recurrence pattern: daily, weekly, or monthly
- When the recurring task is marked as complete, a new instance will be automatically created with the next occurrence date

### Setting Due Dates and Times
- Add due dates/times to tasks in the format 'YYYY-MM-DD HH:MM'
- The app will highlight overdue tasks and show upcoming reminders in the task list
- Console alerts will be shown on application startup for overdue and upcoming tasks

### Viewing Reminders
- Overdue tasks will be marked with [!!!] and highlighted in red
- Upcoming tasks will be marked with [⏰] and highlighted in yellow
- Recurring tasks will be marked with [↻]

### Managing Advanced Settings
- Use the new menu options to set recurrence patterns and due dates/times
- View a summary of reminders from the main menu

## Menu Options
The main menu includes new options for advanced features:
- Set recurring pattern on task
- Set due date & time on task
- View reminders summary

## Testing
Manual console testing is recommended:
1. Create recurring tasks with different patterns (daily, weekly, monthly)
2. Test marking recurring tasks as complete to verify auto-creation of new instances
3. Set due dates/times and verify reminder functionality
4. Check overdue and upcoming task indicators
5. Verify all basic and intermediate functionality still works without regression