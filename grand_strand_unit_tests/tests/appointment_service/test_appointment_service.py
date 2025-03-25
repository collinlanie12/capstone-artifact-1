"""
test_appointment_service.py

This module contains unit tests for the AppointmentService class.

Author: Collin Lanier
Date: 2025-03-21
"""

from datetime import datetime, timedelta

from appointment_service.appointment import Appointment
from appointment_service.appointment_service import AppointmentService


# Helper function to create a valid future datetime
def future_date(seconds=100):
    return datetime.now() + timedelta(seconds=seconds)


# ----------------------------
# Test: Adding an appointment
# ----------------------------
def test_add_appointment():
    service = AppointmentService()
    appointment = Appointment("001", future_date(), "Football Practice")

    # Add should return True the first time
    assert service.add_appointment(appointment) is True

    # Adding the same appointment again should return False
    assert service.add_appointment(appointment) is False


# ----------------------------
# Test: Deleting an appointment
# ----------------------------
def test_delete_appointment():
    service = AppointmentService()
    appointment = Appointment("002", future_date(), "Tennis Practice")

    # Add first so that we can delete it
    service.add_appointment(appointment)

    # Deleting appointment should return True
    assert service.delete_appointment("002") is True

    # Deleting the appointment again should return False
    assert service.delete_appointment("002") is False
