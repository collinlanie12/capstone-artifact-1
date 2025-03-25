package ContactService;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ContactServiceTest {

    // Test adding a contact
    @Test
    public void testAddContact() {
        ContactService contactService = new ContactService();
        Contact contact = new Contact("001", "Collin", "Lanier", "7047770707", "101 Seasme St");
        contactService.addContact(contact);
    }

    // Test to update a contacts first name
    @Test
    public void testUpdateContactFirstName() {
        ContactService contactService = new ContactService();
        Contact contact = new Contact("001", "Collin", "Lanier", "7047770707", "101 Seasme St");
        contactService.addContact(contact);

        // Update the contact's first name
        try {
            contactService.updateContact("001", "Larry", null, null, null);
            assertEquals("Larry", contact.getFirstName());
        } catch (IllegalArgumentException e) {
            fail("Expected an IllegalArgumentException for first name length > 10");
        }
    }

    // Test to update a contacts last name
    @Test
    public void testUpdateContactLastName() {
        ContactService contactService = new ContactService();
        Contact contact = new Contact("001", "Collin", "Lanier", "7047770707", "101 Seasme St");
        contactService.addContact(contact);

        // Update the contact's last name
        try {
            contactService.updateContact("001", null, "Larry", null, null);
            assertEquals("Larry", contact.getLastName());
        } catch (IllegalArgumentException e) {
            fail("Expected an IllegalArgumentException for last name length > 10");
        }
    }

    // Test to update a contacts phone number
    @Test
    public void testUpdateContactPhone() {
        ContactService contactService = new ContactService();
        Contact contact = new Contact("001", "Collin", "Lanier", "7047770707", "101 Seasme St");
        contactService.addContact(contact);

        // Update the contact's phone number
        try {
            contactService.updateContact("001", null, null, "7047770707", null);
            assertEquals("7047770707", contact.getPhone());
        } catch (IllegalArgumentException e) {
            fail("Expected an IllegalArgumentException for phone number length != 10");
        }
    }

    // Test to update a contacts address
    @Test
    public void testUpdateContactAddress() {
        ContactService contactService = new ContactService();
        Contact contact = new Contact("001", "Collin", "Lanier", "7047770707", "101 Seasme St");
        contactService.addContact(contact);

        // Update the contact's address
        try {
            contactService.updateContact("001", null, null, null, "102 Seasme St");
            assertEquals("102 Seasme St", contact.getAddress());
        } catch (IllegalArgumentException e) {
            fail("Expected an IllegalArgumentException for address length > 30");
        }


    }

    // Test deleting a contact
    @Test
    public void testDeleteContact() {
        ContactService contactService = new ContactService();
        Contact contact = new Contact("001", "Collin", "Lanier", "7047770707", "101 Seasme St");
        contactService.addContact(contact);

        // Delete the contact
        contactService.deleteContact("001");

        // Check if the contact was deleted
        try {
            contactService.deleteContact("001");
            fail("Expected an IllegalArgumentException for contact ID does not exist");
        } catch (IllegalArgumentException e) {
            assertEquals("Contact ID does not exist", e.getMessage());
        }
    }

}
