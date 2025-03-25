"""
contact.py

This module defines the Contact class. Used to show a contact with a unique ID, name, phone number, and address. It
includes the logic for initialization and modification of attributes.

Author: Collin Lanier
Date: 2025-03-19
"""


class Contact:
    """
    Represents a contact with a unique ID, name, phone number, and address.
    Validation is done on creation and modification.
    """

    def __init__(self, contact_id: str, first_name: str, last_name: str, phone_number: str, address: str):
        """
        Initializes a new Contact instance with validation

        :param contact_id: Unique string ID (must be less than 10 characters)
        :param first_name: First name string for a contact (must be less than 10 characters)
        :param last_name: Last name string for a contact (must be less than 10 characters)
        :param phone_number: Phone number for a contact (must be exactly 10 digits)
        :param address: Address for a contact (must be less than 30 characters)
        :raises ValueError: If an input is invalid
        """
        if contact_id is None or len(contact_id) > 10:
            raise ValueError("Contact ID is invalid")
        self._contact_id = contact_id

        # Declare all instance attributes
        self._first_name = ""
        self._last_name = ""
        self._phone_number = ""
        self._address = ""

        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_phone_number(phone_number)
        self.set_address(address)

    # Getters
    def get_contact_id(self) -> str:
        """Returns the Contact ID"""
        return self._contact_id

    def get_first_name(self) -> str:
        """Returns the first name of a contact"""
        return self._first_name

    def get_last_name(self) -> str:
        """Returns the last name of a contact"""
        return self._last_name

    def get_phone_number(self) -> str:
        """Returns the phone number of a contact"""
        return self._phone_number

    def get_address(self) -> str:
        """Returns the address of a contact"""
        return self._address

    # Setters with validation
    def set_first_name(self, first_name: str):
        if first_name is None or len(first_name) > 10:
            raise ValueError("First name is invalid")
        self._first_name = first_name

    def set_last_name(self, last_name: str):
        if last_name is None or len(last_name) > 10:
            raise ValueError("Last name is invalid")
        self._last_name = last_name

    def set_phone_number(self, phone_number: str):
        if phone_number is None or len(phone_number) != 10 or not phone_number.isdigit():
            raise ValueError("Phone number is invalid, Digits Only")
        self._phone_number = phone_number

    def set_address(self, address: str):
        if address is None or len(address) > 30:
            raise ValueError("Invalid address")
        self._address = address
