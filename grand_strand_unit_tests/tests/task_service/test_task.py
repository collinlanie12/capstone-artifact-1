"""
test_task.py

This module contains unit tests for the Task class using pytest.

Author: Collin Lanier
Date: 2025-03-23
"""

import pytest
from task_service.task import Task


# ----------------------------
# Test: Creating a valid task
# ----------------------------
def test_create_valid_task():
    task = Task("001", "Task 101", "Homework for the night.")
    assert task.get_task_id() == "001"
    assert task.get_name() == "Task 101"
    assert task.get_description() == "Homework for the night."


# ----------------------------
# Test: Invalid task ID
# ----------------------------
def test_invalid_task_id():
    with pytest.raises(ValueError, match="Task ID cannot be longer than 10 characters"):
        Task("1234567891011", "Task 102", "Study Piano for the day.")


# ----------------------------
# Test: Null task ID
# ----------------------------
def test_null_task_id():
    with pytest.raises(ValueError, match="Task ID must not be null"):
        Task(None, "Task 103", "Practice soccer in the afternoon")


# ----------------------------
# Test: Invalid name
# ----------------------------
def test_invalid_name():
    with pytest.raises(ValueError, match="Name cannot be longer than 20 characters"):
        Task("002", "This Task is very important to me", "Practice web development")


# ----------------------------
# Test: Null name
# ----------------------------
def test_null_name():
    with pytest.raises(ValueError, match="Name must not be null"):
        Task("003", None, "Walk the dog")


# ----------------------------
# Test: Invalid description
# ----------------------------
def test_invalid_description():
    with pytest.raises(ValueError, match="Description cannot be longer than 50 characters"):
        Task("004", "Task 104", "Get a car wash for the dinner and pick up new suit and tie")


# ----------------------------
# Test: Null description
# ----------------------------
def test_null_description():
    with pytest.raises(ValueError, match="Description must not be null"):
        Task("005", "Task 105", None)
