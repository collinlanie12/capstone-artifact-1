package ContactService;
import java.util.HashMap;
import java.util.Map;

public class ContactService {
    // Map to store the contacts
    private final Map<String, Contact> contacts = new HashMap<>();

    // Method to add a contact
    public void addContact(Contact contact) {
        // Check if the contact already exists
        if (contacts.containsKey(contact.getContactId())) {
            throw new IllegalArgumentException("Contact ID already exists");
        }
        // Add the contact
        contacts.put(contact.getContactId(), contact);
    }

    //method to delete a contact per contactId
    public void deleteContact(String contactId) {
        // Check if the contact exists
        if (!contacts.containsKey(contactId)) {
            throw new IllegalArgumentException("Contact ID does not exist");
        }
        // Remove the contact
        contacts.remove(contactId);
    }

    // Method to update a contact
    public void updateContact(String contactId, String firstName, String lastName, String phone, String address) {
        // Check if the contact exists
        if (!contacts.containsKey(contactId)) {
            throw new IllegalArgumentException("Contact ID does not exist");
        }
        // Get the contact
        Contact contact = contacts.get(contactId);
        if (firstName != null) {
            contact.setFirstName(firstName);
        }
        if (lastName != null) {
            contact.setLastName(lastName);
        }
        if (phone != null) {
            contact.setPhone(phone);
        }
        if (address != null) {
            contact.setAddress(address);
        }
    }
}
