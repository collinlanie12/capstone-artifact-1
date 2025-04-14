"""
test_contact.py

This module contains unit tests for the Contact class using pytest.

Author: Collin Lanier
Date: 2025-03-22
"""

import pytest
from contact_service.contact import Contact


# ----------------------------
# Test: Creating a valid contact
# ----------------------------
def test_create_valid_contact():
    contact = Contact("001", "Toby", "Mcguire", "2521015563", "101 Spider-Man Ln")

    assert contact.get_contact_id() == "001"
    assert contact.get_first_name() == "Toby"
    assert contact.get_last_name() == "Mcguire"
    assert contact.get_phone_number() == "2521015563"
    assert contact.get_address() == "101 Spider-Man Ln"


# ----------------------------
# Test: Invalid contact ID
# ----------------------------
def test_invalid_contact_id():
    with pytest.raises(ValueError, match="Contact ID is invalid"):
        Contact(None, "Ryan", "Reynolds", "7042120057", "202 Marvel St")  # Null contact ID

    with pytest.raises(ValueError, match="Contact ID is invalid"):
        Contact("1234567891011", "Bradley", "Cooper", "9198723341", "303 Rocket Ave")  # Longer than 10 characters


# ----------------------------
# Test: Invalid first name
# ----------------------------
def test_invalid_first_name():
    with pytest.raises(ValueError, match="First name is invalid"):
        Contact("002", None, "Swift", "5552325678", "404 Reputation St")  # Null first name

    with pytest.raises(ValueError, match="First name is invalid"):
        Contact("003", "SamuelNickFuryMarvel", "Jackson", "9198723341", "505 Pulp St")  # Longer than 10 characters


# ----------------------------
# Test: Invalid last name
# ----------------------------
def test_invalid_last_name():
    with pytest.raises(ValueError, match="Last name is invalid"):
        Contact("004", "Viola", None, "7770001234", "606 DC Ln")  # Null last name

    with pytest.raises(ValueError, match="Last name is invalid"):
        Contact("005", "Tom", "HanksWilsonIsland", "8882120592", "707 Castaway Ave")  # Longer than 10 characters


# ----------------------------
# Test: Invalid phone number
# ----------------------------
def test_invalid_phone_number():
    with pytest.raises(ValueError, match="Phone number is invalid, Digits Only"):
        Contact("006", "Kerry", "Washington", None, "808 Emmy St")  # Null phone number

    with pytest.raises(ValueError, match="Phone number is invalid, Digits Only"):
        Contact("007", "Ben", "Afleck", "20255588889999", "909 Batman Ave")  # Longer than 10 characters

    with pytest.raises(ValueError, match="Phone number is invalid, Digits Only"):
        Contact("008", "Will", "Smith", "857oke3256", "1001 Fresh Prince Ln ")  # Includes other characters instead of
        # all digits


# ----------------------------
# Test: Invalid address
# ----------------------------
def test_invalid_address():
    with pytest.raises(ValueError, match="Invalid address"):
        Contact("009", "Collin", "Lanier", "2223334444", None)  # Null address

    with pytest.raises(ValueError, match="Invalid address"):
        Contact("1001", "Tom", "Cruise", "7572223333", "1002 Many Mission Impossible Movies And Many More")  # Longer
        # than 30 characters
