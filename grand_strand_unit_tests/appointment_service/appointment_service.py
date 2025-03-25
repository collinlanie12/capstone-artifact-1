"""
appointment_service.py

This module defines the AppointmentService class, which has the functionality to add and delete Appointment
instances by their ID.

Author: Collin Lanier
Date: 2025-03-19
"""
from typing import Dict

from appointment_service.appointment import Appointment


class AppointmentService:
    """
    Controls the collection of appointments using a dictionary.
    Provides methods to add and delete appointments by their ID.
    """

    def __init__(self):
        """
        Initialize an empty dictionary to store the appointment instances.
        The keys are the appointment ID's and the values are Appointment objects.
        """
        self._appointments: Dict[str, Appointment] = {}

    def add_appointment(self, appointment: Appointment) -> bool:
        """
        Adds the appointment to the service.

        :param appointment: The Appointment instance to add
        :return: Is True if appointment is added, False if the ID already exists
        """
        appointment_id = appointment.get_appointment_id()
        if appointment_id in self._appointments:
            return False
        self._appointments[appointment_id] = appointment
        return True

    def delete_appointment(self, appointment_id: str) -> bool:
        """
        Deletes an appointment by the unique ID.

        :param appointment_id: The ID of the appointment to delete
        :return: Is True if the appointment is deleted correctly, False if it is not found
        """
        if appointment_id not in self._appointments:
            return False
        del self._appointments[appointment_id]
        return True
