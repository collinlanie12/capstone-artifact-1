"""
test_appointment.py

This module contains unit tests for the Appointment class using pytest.

Author Collin Lanier
Date: 2025-03-21
"""

import pytest
from datetime import datetime, timedelta
from appointment_service.appointment import Appointment


# Helper function to create a future date
def future_date(seconds=100):
    return datetime.now() + timedelta(seconds=seconds)


# ----------------------------
# Test: Successful creation
# ----------------------------
def test_create_appointment():
    appointment = Appointment("001", future_date(), "Doctor's Appointment")
    assert appointment.get_appointment_id() == "001"
    assert appointment.get_appointment_date() is not None
    assert appointment.get_description() == "Doctor's Appointment"


# ----------------------------
# Test: Invalid appointment ID
# ----------------------------
def test_invalid_appointment_id():
    with pytest.raises(ValueError, match="Appointment ID is invalid"):
        Appointment(None, future_date(), "Dentist Appointment")  # Null ID
    with pytest.raises(ValueError, match="Appointment ID is invalid"):
        Appointment("1234567891011", future_date(), "Car Inspection")  # Longer than 10 characters


# ----------------------------
# Test: Invalid appointment date
# ----------------------------
def test_invalid_appointment_date():
    with pytest.raises(ValueError, match="Appointment date is invalid"):
        Appointment("002", None, "Physical Therapy")  # Null Date
    with pytest.raises(ValueError, match="Appointment date is invalid"):
        Appointment("003", datetime.now() - timedelta(days=1), "Soccer Practice")  # Past Date


# ----------------------------
# Test: Invalid description
# ----------------------------
def test_invalid_description():
    with pytest.raises(ValueError, match="Description is invalid"):
        Appointment("004", future_date(), None)  # Null Description
    with pytest.raises(ValueError, match="Description is invalid"):
        Appointment("005", future_date(), "C" * 103)  # 103-character description, longer than 50 characters
