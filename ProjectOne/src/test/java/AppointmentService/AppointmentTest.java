package AppointmentService;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Date;

public class AppointmentTest {

    // Test creating an appointment
    @Test
    public void testCreateAppointment() {
        // Create an appointment object
        Appointment appointment = new Appointment("001", new Date(System.currentTimeMillis() + 100000), "Appointment 1");

        // Check if the appointment ID is equal to "001"
        assertEquals("001", appointment.getAppointmentId());
        // Check if the appointment is not null
        assertNotNull(appointment.getAppointmentDate());
        // Check if the description is equal to "Appointment 1"
        assertEquals("Appointment 1", appointment.getDescription());
    }

    // Test creating an appointment with an invalid appointment ID
    @Test
    public void testInvalidAppointmentID() {
        // Create an appointment object with an invalid appointment ID as null
        try {
            Appointment appointment = new Appointment(null, new Date(System.currentTimeMillis() + 100000), "Appointment 1");
        } catch (IllegalArgumentException e) {
            assertEquals("Appointment ID invalid", e.getMessage());
        }

        // Create an appointment object with an invalid appointment ID
        try {
            Appointment appointment = new Appointment("00000000001", new Date(System.currentTimeMillis() + 100000), "Appointment 1");
        } catch (IllegalArgumentException e) {
            assertEquals("Appointment ID invalid", e.getMessage());
        }
    }

    // Test creating an appointment with an invalid appointment date
    @Test
    public void testInvalidAppointmentDate() {
        // Create an appointment object with an invalid appointment date as null
        try {
            Appointment appointment = new Appointment("001", null, "Appointment 1");
        } catch (IllegalArgumentException e) {
            assertEquals("Appointment date invalid", e.getMessage());
        }

        // Create an appointment object with an invalid appointment date in the past
        try {
            Appointment appointment = new Appointment("001", new Date(System.currentTimeMillis() - 100000), "Appointment 1");
        } catch (IllegalArgumentException e) {
            assertEquals("Appointment date invalid", e.getMessage());
        }

    }

    // Test creating an appointment with an invalid description
    @Test
    public void testInvalidDescription() {
        // Create an appointment object with an invalid description as null
        try {
            Appointment appointment = new Appointment("001", new Date(System.currentTimeMillis() + 100000), null);
        } catch (IllegalArgumentException e) {
            assertEquals("Description invalid", e.getMessage());
        }

        // Create an appointment object with an invalid description
        try {
            Appointment appointment = new Appointment("001", new Date(System.currentTimeMillis() + 100000), "Description 1 Description 1 Description 1 Description 1 Description 1");
        } catch (IllegalArgumentException e) {
            assertEquals("Description invalid", e.getMessage());
        }
    }
}
