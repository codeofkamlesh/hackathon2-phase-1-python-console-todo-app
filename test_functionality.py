#!/usr/bin/env python3
"""
Test script to verify the new functionality works correctly.
"""

import sys
import os

# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_app.services.todo_manager import TodoManager

def test_new_functionality():
    print("Testing new functionality...")

    # Create a TodoManager instance
    manager = TodoManager()

    # Test 1: Add a task with priority, tags, and due date
    print("\n1. Testing task creation with new fields...")
    task_id = manager.add_task(
        title="Test Task",
        description="This is a test task",
        priority="high",
        tags=["work", "important"],
        due_date="2025-12-31"
    )
    print(f"Task created with ID: {task_id}")

    # Get the task to verify it was created correctly
    task = manager.get_task_by_id(task_id)
    print(f"Task details - Title: {task.title}, Priority: {task.priority}, Tags: {task.tags}, Due Date: {task.due_date}")

    # Test 2: Update task priority
    print("\n2. Testing priority update...")
    manager.set_priority(task_id, "low")
    updated_task = manager.get_task_by_id(task_id)
    print(f"Updated priority: {updated_task.priority}")

    # Test 3: Add and remove tags
    print("\n3. Testing tag management...")
    manager.add_tag(task_id, "urgent")
    task_with_new_tag = manager.get_task_by_id(task_id)
    print(f"Tags after adding 'urgent': {task_with_new_tag.tags}")

    manager.remove_tag(task_id, "work")
    task_after_remove = manager.get_task_by_id(task_id)
    print(f"Tags after removing 'work': {task_after_remove.tags}")

    # Test 4: Search functionality
    print("\n4. Testing search functionality...")
    manager.add_task("Another test task", "This is another task for testing", priority="medium", tags=["test"])
    search_results = manager.search_tasks("test")
    print(f"Search results for 'test': {len(search_results)} tasks found")
    for task in search_results:
        print(f"  - {task.title}")

    # Test 5: Filter functionality
    print("\n5. Testing filter functionality...")
    filtered_by_priority = manager.filter_tasks(priority="low")
    print(f"Tasks with low priority: {len(filtered_by_priority)}")

    # Test 6: Sort functionality
    print("\n6. Testing sort functionality...")
    all_tasks = manager.get_all_tasks()
    print(f"Total tasks before sorting: {len(all_tasks)}")

    sorted_by_priority = manager.sort_tasks(by="priority")
    print("Tasks sorted by priority:")
    for task in sorted_by_priority:
        print(f"  - {task.title} (Priority: {task.priority})")

    print("\nAll tests completed successfully!")

if __name__ == "__main__":
    test_new_functionality()