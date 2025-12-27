"""
CLI Menu for the Todo App.

This module provides the interactive menu interface for the todo application.
It handles user input and navigation between different operations.
"""

from typing import Optional
from todo_app.services.todo_manager import TodoManager


class TodoMenu:
    """
    Main menu class for the Todo application.
    """

    def __init__(self):
        """Initialize the TodoMenu."""
        self.todo_manager = TodoManager()

    def display_menu(self):
        """Display the main menu options."""
        print("\n--- Todo App Menu ---")
        print("1. Add new task")
        print("2. View all tasks")
        print("3. Update task")
        print("4. Delete task")
        print("5. Mark task as complete")
        print("6. Mark task as incomplete")
        print("7. Set task priority")
        print("8. Manage task tags")
        print("9. Search tasks")
        print("10. Filter tasks")
        print("11. Sort tasks")
        print("12. Exit")
        print("----------------------")

    def get_user_choice(self) -> str:
        """Get user's menu choice."""
        try:
            choice = input("Enter your choice (1-7): ").strip()
            return choice
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            return "7"

    def add_task(self):
        """Add a new task."""
        try:
            title = input("Enter task title: ").strip()
            if not title:
                print("Task title cannot be empty.")
                return

            description = input("Enter task description (optional, press Enter to skip): ").strip()

            # Get priority
            priority = input("Enter priority (high/medium/low, press Enter for 'medium'): ").strip().lower()
            if not priority:
                priority = "medium"
            elif priority not in ["high", "medium", "low"]:
                print("Invalid priority. Using 'medium' as default.")
                priority = "medium"

            # Get tags
            tags_input = input("Enter tags separated by commas (optional, press Enter to skip): ").strip()
            if tags_input:
                tags = [tag.strip() for tag in tags_input.split(',')]
            else:
                tags = []

            # Get due date
            due_date = input("Enter due date (YYYY-MM-DD, optional, press Enter to skip): ").strip()
            if not due_date:
                due_date = None

            task_id = self.todo_manager.add_task(title, description, priority, tags, due_date)
            print(f"Task added successfully with ID: {task_id}")
        except ValueError as e:
            print(f"Error adding task: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def view_tasks(self):
        """View all tasks."""
        tasks = self.todo_manager.get_all_tasks()

        if not tasks:
            print("No tasks found.")
            return

        print("\n--- Your Tasks ---")
        for task in tasks:
            status = "✓" if task.completed else "○"
            priority_indicator = self._get_priority_indicator(task.priority)
            tags_str = f" [{', '.join(task.tags)}]" if task.tags else ""
            print(f"{status} ID: {task.id} | {priority_indicator} | Title: {task.title}{tags_str}")
            if task.description:
                print(f"    Description: {task.description}")
            if task.due_date:
                print(f"    Due Date: {task.due_date}")
        print("------------------")

    def update_task(self):
        """Update an existing task."""
        try:
            task_id_str = input("Enter task ID to update: ").strip()
            if not task_id_str:
                print("Task ID is required.")
                return

            task_id = int(task_id_str)

            # Get the current task to show existing values
            current_task = self.todo_manager.get_task_by_id(task_id)
            print(f"Current title: {current_task.title}")
            print(f"Current description: {current_task.description}")
            print(f"Current priority: {current_task.priority}")
            print(f"Current tags: {', '.join(current_task.tags) if current_task.tags else 'None'}")
            print(f"Current due date: {current_task.due_date if current_task.due_date else 'None'}")
            print(f"Current status: {'Completed' if current_task.completed else 'Incomplete'}")

            new_title = input(f"Enter new title (or press Enter to keep '{current_task.title}'): ").strip()
            if new_title == "":
                new_title = None  # Use None to indicate no change

            new_description = input(f"Enter new description (or press Enter to keep current): ").strip()
            if new_description == "":
                new_description = None  # Use None to indicate no change

            new_priority = input(f"Enter new priority (high/medium/low, or press Enter to keep '{current_task.priority}'): ").strip().lower()
            if new_priority == "":
                new_priority = None  # Use None to indicate no change
            elif new_priority not in ["high", "medium", "low"]:
                print("Invalid priority. Keeping current priority.")
                new_priority = None

            new_tags_input = input(f"Enter new tags separated by commas (or press Enter to keep current): ").strip()
            if new_tags_input == "":
                new_tags = None  # Use None to indicate no change
            else:
                new_tags = [tag.strip() for tag in new_tags_input.split(',')]  # Use new value

            new_due_date = input(f"Enter new due date (YYYY-MM-DD, or press Enter to keep current): ").strip()
            if new_due_date == "":
                new_due_date = None  # Use None to indicate no change
            elif new_due_date.lower() == "none":
                new_due_date = None  # Explicitly set to None

            new_status_input = input(f"Enter new status (completed/incomplete, or press Enter to keep current): ").strip().lower()
            if new_status_input == "":
                new_completed = None  # Use None to indicate no change
            elif new_status_input == "completed":
                new_completed = True
            elif new_status_input == "incomplete":
                new_completed = False
            else:
                print("Invalid status. Keeping current status.")
                new_completed = None

            # Perform the update
            self.todo_manager.update_task(task_id, new_title, new_description,
                                       new_priority, new_tags, new_due_date, new_completed)
            print("Task updated successfully.")
        except ValueError as e:
            print(f"Error updating task: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def delete_task(self):
        """Delete a task."""
        try:
            task_id_str = input("Enter task ID to delete: ").strip()
            if not task_id_str:
                print("Task ID is required.")
                return

            task_id = int(task_id_str)
            success = self.todo_manager.delete_task(task_id)
            if success:
                print(f"Task with ID {task_id} deleted successfully.")
            else:
                print(f"Failed to delete task with ID {task_id}.")
        except ValueError as e:
            print(f"Error deleting task: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def mark_task_complete(self):
        """Mark a task as complete."""
        try:
            task_id_str = input("Enter task ID to mark as complete: ").strip()
            if not task_id_str:
                print("Task ID is required.")
                return

            task_id = int(task_id_str)
            success = self.todo_manager.mark_complete(task_id)
            if success:
                print(f"Task with ID {task_id} marked as complete.")
            else:
                print(f"Failed to mark task with ID {task_id} as complete.")
        except ValueError as e:
            print(f"Error marking task as complete: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def mark_task_incomplete(self):
        """Mark a task as incomplete."""
        try:
            task_id_str = input("Enter task ID to mark as incomplete: ").strip()
            if not task_id_str:
                print("Task ID is required.")
                return

            task_id = int(task_id_str)
            success = self.todo_manager.mark_incomplete(task_id)
            if success:
                print(f"Task with ID {task_id} marked as incomplete.")
            else:
                print(f"Failed to mark task with ID {task_id} as incomplete.")
        except ValueError as e:
            print(f"Error marking task as incomplete: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def set_task_priority(self):
        """Set the priority of a task."""
        try:
            task_id_str = input("Enter task ID to set priority: ").strip()
            if not task_id_str:
                print("Task ID is required.")
                return

            task_id = int(task_id_str)

            # Validate the task exists
            current_task = self.todo_manager.get_task_by_id(task_id)

            print(f"Current priority: {current_task.priority}")
            print("Available priorities: high, medium, low")
            new_priority = input("Enter new priority: ").strip().lower()

            if new_priority not in ["high", "medium", "low"]:
                print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
                return

            success = self.todo_manager.set_priority(task_id, new_priority)
            if success:
                print(f"Priority updated to '{new_priority}' for task ID {task_id}.")
            else:
                print(f"Failed to update priority for task ID {task_id}.")
        except ValueError as e:
            print(f"Error setting task priority: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def manage_task_tags(self):
        """Manage tags for a task."""
        try:
            task_id_str = input("Enter task ID to manage tags: ").strip()
            if not task_id_str:
                print("Task ID is required.")
                return

            task_id = int(task_id_str)

            # Validate the task exists
            current_task = self.todo_manager.get_task_by_id(task_id)

            print(f"Current tags: {', '.join(current_task.tags) if current_task.tags else 'None'}")
            print("Choose an option:")
            print("1. Add tag")
            print("2. Remove tag")
            print("3. Set all tags")

            option = input("Enter option (1-3): ").strip()

            if option == "1":
                tag = input("Enter tag to add: ").strip()
                if tag:
                    success = self.todo_manager.add_tag(task_id, tag)
                    if success:
                        print(f"Tag '{tag}' added to task ID {task_id}.")
                    else:
                        print(f"Failed to add tag to task ID {task_id}.")
                else:
                    print("Tag cannot be empty.")
            elif option == "2":
                if not current_task.tags:
                    print("No tags to remove.")
                    return
                tag = input("Enter tag to remove: ").strip()
                if tag in current_task.tags:
                    success = self.todo_manager.remove_tag(task_id, tag)
                    if success:
                        print(f"Tag '{tag}' removed from task ID {task_id}.")
                    else:
                        print(f"Failed to remove tag from task ID {task_id}.")
                else:
                    print(f"Tag '{tag}' not found in task.")
            elif option == "3":
                tags_input = input("Enter tags separated by commas: ").strip()
                if tags_input:
                    tags = [tag.strip() for tag in tags_input.split(',')]
                    success = self.todo_manager.set_tags(task_id, tags)
                    if success:
                        print(f"Tags updated for task ID {task_id}: {', '.join(tags)}")
                    else:
                        print(f"Failed to update tags for task ID {task_id}.")
                else:
                    print("Tags input cannot be empty.")
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
        except ValueError as e:
            print(f"Error managing task tags: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def search_tasks(self):
        """Search tasks by keyword."""
        try:
            keyword = input("Enter keyword to search for: ").strip()
            if not keyword:
                print("Keyword is required.")
                return

            matching_tasks = self.todo_manager.search_tasks(keyword)

            if not matching_tasks:
                print("No tasks found matching your search.")
                return

            print(f"\n--- Search Results for '{keyword}' ---")
            for task in matching_tasks:
                status = "✓" if task.completed else "○"
                priority_indicator = self._get_priority_indicator(task.priority)
                tags_str = f" [{', '.join(task.tags)}]" if task.tags else ""
                print(f"{status} ID: {task.id} | {priority_indicator} | Title: {task.title}{tags_str}")
                if task.description:
                    print(f"    Description: {task.description}")
                if task.due_date:
                    print(f"    Due Date: {task.due_date}")
            print("----------------------------------------")
        except ValueError as e:
            print(f"Error searching tasks: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def filter_tasks(self):
        """Filter tasks by status, priority, or due date."""
        try:
            print("Filter options:")
            print("1. By status (completed/incomplete)")
            print("2. By priority (high/medium/low)")
            print("3. By due date")
            print("4. By multiple criteria")

            option = input("Enter filter option (1-4): ").strip()

            status = None
            priority = None
            due_date = None

            if option == "1":
                status_choice = input("Enter status (completed/incomplete): ").strip().lower()
                if status_choice in ["completed", "incomplete"]:
                    status = status_choice
                else:
                    print("Invalid status. Please enter 'completed' or 'incomplete'.")
                    return
            elif option == "2":
                priority_choice = input("Enter priority (high/medium/low): ").strip().lower()
                if priority_choice in ["high", "medium", "low"]:
                    priority = priority_choice
                else:
                    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
                    return
            elif option == "3":
                due_date = input("Enter due date (YYYY-MM-DD): ").strip()
                # Basic validation - in a real app, we'd validate the format
            elif option == "4":
                status_choice = input("Enter status (completed/incomplete, press Enter to skip): ").strip().lower()
                if status_choice and status_choice in ["completed", "incomplete"]:
                    status = status_choice
                elif status_choice and status_choice not in ["completed", "incomplete"]:
                    print("Invalid status. Please enter 'completed' or 'incomplete'.")
                    return

                priority_choice = input("Enter priority (high/medium/low, press Enter to skip): ").strip().lower()
                if priority_choice and priority_choice in ["high", "medium", "low"]:
                    priority = priority_choice
                elif priority_choice and priority_choice not in ["high", "medium", "low"]:
                    print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
                    return

                due_date_input = input("Enter due date (YYYY-MM-DD, press Enter to skip): ").strip()
                if due_date_input:
                    due_date = due_date_input
            else:
                print("Invalid option. Please enter 1, 2, 3, or 4.")
                return

            filtered_tasks = self.todo_manager.filter_tasks(status=status, priority=priority, due_date=due_date)

            if not filtered_tasks:
                print("No tasks found matching your filter criteria.")
                return

            print("\n--- Filtered Tasks ---")
            for task in filtered_tasks:
                status = "✓" if task.completed else "○"
                priority_indicator = self._get_priority_indicator(task.priority)
                tags_str = f" [{', '.join(task.tags)}]" if task.tags else ""
                print(f"{status} ID: {task.id} | {priority_indicator} | Title: {task.title}{tags_str}")
                if task.description:
                    print(f"    Description: {task.description}")
                if task.due_date:
                    print(f"    Due Date: {task.due_date}")
            print("----------------------")
        except ValueError as e:
            print(f"Error filtering tasks: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def sort_tasks(self):
        """Sort tasks by priority, due date, or title."""
        try:
            print("Sort options:")
            print("1. By priority (high to low)")
            print("2. By due date")
            print("3. By title (alphabetically)")

            option = input("Enter sort option (1-3): ").strip()

            if option == "1":
                sort_by = "priority"
            elif option == "2":
                sort_by = "due_date"
            elif option == "3":
                sort_by = "title"
            else:
                print("Invalid option. Please enter 1, 2, or 3.")
                return

            sorted_tasks = self.todo_manager.sort_tasks(by=sort_by)

            if not sorted_tasks:
                print("No tasks to display.")
                return

            print(f"\n--- Sorted Tasks ({sort_by}) ---")
            for task in sorted_tasks:
                status = "✓" if task.completed else "○"
                priority_indicator = self._get_priority_indicator(task.priority)
                tags_str = f" [{', '.join(task.tags)}]" if task.tags else ""
                print(f"{status} ID: {task.id} | {priority_indicator} | Title: {task.title}{tags_str}")
                if task.description:
                    print(f"    Description: {task.description}")
                if task.due_date:
                    print(f"    Due Date: {task.due_date}")
            print("-------------------------------")
        except ValueError as e:
            print(f"Error sorting tasks: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def _get_priority_indicator(self, priority: str) -> str:
        """Get the priority indicator for display."""
        if priority == "high":
            return "[H]"
        elif priority == "medium":
            return "[M]"
        elif priority == "low":
            return "[L]"
        else:
            return "[?]"  # Fallback for invalid priority

    def run(self):
        """Run the main menu loop."""
        print("Welcome to the Todo App!")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_complete()
            elif choice == "6":
                self.mark_task_incomplete()
            elif choice == "7":
                self.set_task_priority()
            elif choice == "8":
                self.manage_task_tags()
            elif choice == "9":
                self.search_tasks()
            elif choice == "10":
                self.filter_tasks()
            elif choice == "11":
                self.sort_tasks()
            elif choice == "12":
                print("Thank you for using the Todo App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 12.")