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
        print("7. Exit")
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

            task_id = self.todo_manager.add_task(title, description)
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
            print(f"{status} ID: {task.id} | Title: {task.title}")
            if task.description:
                print(f"    Description: {task.description}")
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

            new_title = input(f"Enter new title (or press Enter to keep '{current_task.title}'): ").strip()
            if new_title == "":
                new_title = None  # Use None to indicate no change

            new_description = input(f"Enter new description (or press Enter to keep current): ").strip()
            if new_description == "":
                new_description = None  # Use None to indicate no change

            # Perform the update
            self.todo_manager.update_task(task_id, new_title, new_description)
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
                print("Thank you for using the Todo App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")