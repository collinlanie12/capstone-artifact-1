"""
contact_service.py

This module defines the ContactService class, which handles a collection of Contact objects. It contains methods to
add, update, and delete contacts using their unique ID.

Author: Collin Lanier
Date: 2025-03-19
"""

from typing import Dict
from contact_service.contact import Contact


class ContactService:
    """
    Controls the collection of contact data using a dictionary. Provides methods for adding, deleting and updating
    contacts.
    """

    def __init__(self):
        """
        Initialize an empty dictionary to store the contacts instances. The keys are the contacts ID's,
        and the values are the Contact objects.
        """
        self._contacts: Dict[str, Contact] = {}

    def add_contact(self, contact: Contact) -> bool:
        """
        Adds a new contact to the service.

        :param contact: The Contact instance to add
        :return:True if a contact was added, False if the ID already exists
        """
        contact_id = contact.get_contact_id()
        if contact_id in self._contacts:
            return False
        self._contacts[contact_id] = contact
        return True

    def delete_contact(self, contact_id: str) -> bool:
        """
        Deletes an existing contact by ID.

        :param contact_id: The ID of the contact to delete
        :return: True if contact was deleted, False if ID does not exist
        """
        if contact_id not in self._contacts:
            return False
        del self._contacts[contact_id]
        return True

    def update_contact(self, contact_id: str, first_name: str = None, last_name: str = None,
                       phone_number: str = None, address: str = None) -> bool:
        """
        Updates the fields of an existing contact, if provided.

        :param contact_id: The ID of the contact to update
        :param first_name: Update first name of contact (not required)
        :param last_name: Update last name of contact (not required)
        :param phone_number: Update phone number of contact (not required)
        :param address: Updated address of contact (not required)
        :return: True if contact was updated, False if contact ID is not found
        """
        if contact_id not in self._contacts:
            return False

        contact = self._contacts[contact_id]

        if first_name is not None:
            contact.set_first_name(first_name)
        if last_name is not None:
            contact.set_last_name(last_name)
        if phone_number is not None:
            contact.set_phone_number(phone_number)
        if address is not None:
            contact.set_address(address)

        return True
