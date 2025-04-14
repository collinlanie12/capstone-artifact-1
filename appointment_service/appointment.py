"""
appointment.py

This module defines the Appointment class. Used to show an appointment information with validation logic for ID, date,
and description.

Author: Collin Lanier
Date: 2025-03-19
"""

from datetime import datetime


class Appointment:
    """
    This represents a scheduled appointment with a unique ID, date, and description. Validation is done on creation.
    """

    def __init__(self, appointment_id: str, appointment_date: datetime, description: str):
        """
        Initializes an Appointment instance.

        :param appointment_id: Unique string ID (must be less than 10 characters)
        :param appointment_date: datetime object (cannot be set in the past dates)
        :param description: Description of an appointment (must be less than 50 characters)
        :raises ValueError: If an input is invalid
        """
        if appointment_id is None or len(appointment_id) > 10:
            raise ValueError("Appointment ID is invalid")

        if appointment_date is None or appointment_date < datetime.now():
            raise ValueError("Appointment date is invalid")

        if description is None or len(description) > 50:
            raise ValueError("Description is invalid")

        self._appointment_id = appointment_id
        self._appointment_date = appointment_date
        self._description = description

    def get_appointment_id(self) -> str:
        """Returns appointment ID"""
        return self._appointment_id

    def get_appointment_date(self) -> datetime:
        """Returns the appointment date"""
        return self._appointment_date

    def get_description(self) -> str:
        """Returns the appointment description"""
        return self._description
