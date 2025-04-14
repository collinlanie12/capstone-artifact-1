"""
test_task_service.py

This module contains unit tests for the TaskService class.

Author: Collin Lanier
Date: 2025-03-23
"""

from task_service.task import Task
from task_service.task_service import TaskService


# ----------------------------
# Test: Adding a task
# ----------------------------
def test_add_task():
    service = TaskService()
    task = Task("001", "Task 101", "Go to the store")

    assert service.add_task(task) is True

    # Adding the same task again should return False
    assert service.add_task(task) is False


# ----------------------------
# Test: Deleting a task
# ----------------------------
def test_delete_task():
    # Create and add a task first to delete
    service = TaskService()
    task = Task("002", "Task 102", "Get a haircut")
    service.add_task(task)

    assert service.delete_task("002") is True

    # Deleting again should return False
    assert service.delete_task("002") is False


# ----------------------------
# Test: Updating task name
# ----------------------------
def test_update_task_name():
    service = TaskService()
    task = Task("003", "Task 103", "Doctor's appointment")
    service.add_task(task)

    assert service.update_task_name("003", "Task 104") is True
    assert task.get_name() == "Task 104"


# ----------------------------
# Test: Updating task description
# ----------------------------
def test_update_task_description():
    service = TaskService()
    task = Task("004", "Task 105", "Take pet to the vet")
    service.add_task(task)

    assert service.update_task_description("004", "Attend conference meeting")
    assert task.get_description() == "Attend conference meeting"


# ----------------------------
# Test: Getting a task
# ----------------------------
def test_get_task():
    service = TaskService()
    task = Task("005", "Task 106", "Create web dashboard")
    service.add_task(task)

    target_task = service.get_task("005")
    assert target_task is not None
    assert target_task.get_task_id() == "005"
