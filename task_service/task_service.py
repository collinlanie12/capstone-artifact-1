"""
task_service.py

This module defines the TaskService class, which handles a collection of Task objects. It contains methods to
add, update, and delete tasks using their unique ID.

Author: Collin Lanier
Date: 2025-03-19
"""

from typing import Dict, Optional
from task_service.task import Task


class TaskService:
    """
    Controls the collection of task data using a dictionary. Provides methods for adding, deleting and updating
    tasks.
    """

    def __init__(self):
        """
        Initialize an empty dictionary to store the task instances. The keys are the Task ID's,
        and the values are the Task objects.
        """
        self._tasks: Dict[str, Task] = {}

    def add_task(self, task: Task) -> bool:
        """
        Adds a new task to the service.

        :param task: The Task instance to add
        :return: True if task was added, False if the ID already exists
        """
        task_id = task.get_task_id()
        if task_id in self._tasks:
            return False
        self._tasks[task_id] = task
        return True

    def delete_task(self, task_id: str) -> bool:
        """
        Deletes an existing task by its ID

        :param task_id: The unique ID of the task to be deleted
        :return: True if the task was deleted, False if the ID is not found
        """
        if task_id not in self._tasks:
            return False
        del self._tasks[task_id]
        return True

    def update_task_name(self, task_id: str, new_name: str) -> bool:
        """
        Updates the name of a task.

        :param task_id: The task ID to update
        :param new_name: The new name of the task
        :return: True if the update succeeds, False if the task is not found
        """
        if task_id not in self._tasks:
            return False
        self._tasks[task_id].set_name(new_name)
        return True

    def update_task_description(self, task_id: str, new_description: str) -> bool:
        """
        Updates the description of a task.

        :param task_id: The task ID to update
        :param new_description: The new description of the task
        :return: True if the update succeeds, False if the task is not found
        """
        if task_id not in self._tasks:
            return False
        self._tasks[task_id].set_description(new_description)
        return True

    def get_task(self, task_id: str) -> Optional[Task]:
        """
        Gets a task by its ID.

        :param task_id: The ID of the task to retrieve
        :return: The Task object if found, else None
        """
        return self._tasks.get(task_id)
