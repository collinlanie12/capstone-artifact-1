"""
task.py

This module defines the Task class. Used to show a task with a unique ID, name, and description. It
includes validation on creation and modification of attributes.

Author: Collin Lanier
Date: 2025-03-19
"""


class Task:
    """
    Represents a task with a unique ID, name, and description.
    Validation is done on creation and modification.
    """

    def __init__(self, task_id: str, name: str, description: str):
        """
        Initializes a new Task instance.

        :param task_id: Unique string ID (must be less than 10 characters)
        :param name: The Task name (must be less than 20 characters)
        :param description: Description of a task (must be less than 50 characters)
        :raises ValueError: If a field is null or goes over the max length
        """
        if task_id is None:
            raise ValueError("Task ID must not be null")
        if name is None:
            raise ValueError("Name must not be null")
        if description is None:
            raise ValueError("Description must not be null")

        if len(task_id) > 10:
            raise ValueError("Task ID cannot be longer than 10 characters")
        if len(name) > 20:
            raise ValueError("Name cannot be longer than 20 characters")
        if len(description) > 50:
            raise ValueError("Description cannot be longer than 50 characters")

        # Declare all instance attributes
        self._task_id = task_id
        self._name = ""
        self._description = ""

        self.set_name(name)
        self.set_description(description)

    # Getters
    def get_task_id(self) -> str:
        """Returns the task ID"""
        return self._task_id

    def get_name(self) -> str:
        """Returns the name of the task"""
        return self._name

    def get_description(self) -> str:
        """Returns the description of a task"""
        return self._description

    # Setters with validation
    def set_name(self, name: str):
        if name is None:
            raise ValueError("Name must not be null")
        if len(name) > 20:
            raise ValueError("Name cannot be longer than 20 characters")
        self._name = name

    def set_description(self, description: str):
        if description is None:
            raise ValueError("Description must not be null")
        if len(description) > 50:
            raise ValueError("Description cannot be longer than 50 characters")
        self._description = description
