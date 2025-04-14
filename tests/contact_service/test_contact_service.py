"""
test_contact_service.py

This module contains unit tests for the ContactService class.

Author: Collin Lanier
Date: 2025-03-23
"""

from contact_service.contact import Contact
from contact_service.contact_service import ContactService


# ----------------------------
# Test: Adding a contact
# ----------------------------
def test_add_contact():
    service = ContactService()
    contact = Contact("001", "Collin", "Lanier", "7072224321", "101 Sesame st")
    assert service.add_contact(contact) is True

    # Adding the same contact again should return False
    assert service.add_contact(contact) is False


# ----------------------------
# Test: Updating contact first name
# ----------------------------
def test_update_first_name():
    service = ContactService()
    contact = Contact("002", "Zachary", "Lanier", "4042229876", "202 Sesame st")
    service.add_contact(contact)

    assert service.update_contact("002", first_name="Larry") is True
    assert contact.get_first_name() == "Larry"


# ----------------------------
# Test: Updating contact last name
# ----------------------------
def test_update_last_name():
    service = ContactService()
    contact = Contact("003", "Sun", "Moon", "9871234567", "303 Sesame st")
    service.add_contact(contact)

    assert service.update_contact("003", last_name="Earth") is True
    assert contact.get_last_name() == "Earth"


# ----------------------------
# Test: Updating contact phone number
# ----------------------------
def test_update_phone_number():
    service = ContactService()
    contact = Contact("004", "Alexander", "Great", "2223334444", "404 Sesame st")
    service.add_contact(contact)

    assert service.update_contact("004", phone_number="1112223333") is True
    assert contact.get_phone_number() == "1112223333"


# ----------------------------
# Test: Updating contact address
# ----------------------------
def test_update_address():
    service = ContactService()
    contact = Contact("005", "King", "Arthur", "0001112222", "505 Sesame st")
    service.add_contact(contact)

    assert service.update_contact("005", address="606 Sesame st") is True
    assert contact.get_address() == "606 Sesame st"


# ----------------------------
# Test: Deleting a contact
# ----------------------------
def test_delete_contact():
    service = ContactService()
    contact = Contact("006", "Harry", "Potter", "5554443333", "707 Sesame st")
    service.add_contact(contact)

    # First delete should succeed
    assert service.delete_contact("006") is True

    # Second delete on the same ID should return False
    assert service.delete_contact("006") is False
