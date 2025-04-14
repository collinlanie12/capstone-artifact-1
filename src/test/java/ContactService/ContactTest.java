package ContactService;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class ContactTest {

    // Test creating a valid contact
    @Test
    public void testCreateValidContact() {
        Contact contact = new Contact("001", "Collin", "Lanier", "7047770707", "101 Seasme St");
        assertEquals("001", contact.getContactId());
        assertEquals("Collin", contact.getFirstName());
        assertEquals("Lanier", contact.getLastName());
        assertEquals("7047770707", contact.getPhone());
        assertEquals("101 Seasme St", contact.getAddress());
    }

    // Test creating a contact with an invalid contact ID
    @Test
    public void testCreateInvalidContactId() {
        try {
            new Contact(null, "Collin", "Lanier", "7047770707", "101 Seasme St");
            fail("Expected an IllegalArgumentException for null contact ID");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid contact ID", e.getMessage());
        }

        try {
            new Contact("00000000001", "Collin", "Lanier", "7047770707", "101 Seasme St");
            fail("Expected an IllegalArgumentException for contact ID length > 10");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid contact ID", e.getMessage());
        }
    }

    // Test creating a contact with an invalid first name
    @Test
    public void testCreateInvalidFirstName() {
        try {
            new Contact("001", null, "Lanier", "7047770707", "101 Seasme St");
            fail("Expected an IllegalArgumentException for null first name");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid first name", e.getMessage());
        }

        try {
            new Contact("001", "CollinCollin", "Lanier", "7047770707", "101 Seasme St");
            fail("Expected an IllegalArgumentException for first name length > 10");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid first name", e.getMessage());
        }
    }

    // Test creating a contact with an invalid last name
    @Test
    public void testCreateInvalidLastName() {
        try {
            new Contact("001", "Collin", null, "7047770707", "101 Seasme St");
            fail("Expected an IllegalArgumentException for null last name");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid last name", e.getMessage());
        }

        try {
            new Contact("001", "Collin", "LanierLanier", "7047770707", "101 Seasme St");
            fail("Expected an IllegalArgumentException for last name length > 10");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid last name", e.getMessage());
        }
    }

    // Test creating a contact with an invalid phone number
    @Test
    public void testCreateInvalidPhone() {
        try {
            new Contact("001", "Collin", "Lanier", null, "101 Seasme St");
            fail("Expected an IllegalArgumentException for null phone number");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid phone number", e.getMessage());
        }

        try {
            new Contact("001", "Collin", "Lanier", "70477707071", "101 Seasme St");
            fail("Expected an IllegalArgumentException for phone number length != 10");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid phone number", e.getMessage());
        }
    }

    // Test creating a contact with an invalid address
    @Test
    public void testCreateInvalidAddress() {
        try {
            new Contact("001", "Collin", "Lanier", "7047770707", null);
            fail("Expected an IllegalArgumentException for null address");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid address", e.getMessage());
        }

        try {
            new Contact("001", "Collin", "Lanier", "7047770707", "101 Seasme St101 Seasme St101 Seasme St");
            fail("Expected an IllegalArgumentException for address length > 30");
        } catch (IllegalArgumentException e) {
            assertEquals("Invalid address", e.getMessage());
        }
    }
}
