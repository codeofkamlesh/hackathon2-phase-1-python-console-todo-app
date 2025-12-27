#!/usr/bin/env python3
"""
Main entry point for the Todo App.

This is the starting point for the console-based todo application.
The application supports adding, viewing, updating, deleting tasks,
and marking them as complete/incomplete.
"""

from todo_app.cli.menu import TodoMenu


def main():
    """Main function to run the Todo application."""
    print("Initializing menu system...")
    menu = TodoMenu()
    menu.run()


if __name__ == "__main__":
    main()