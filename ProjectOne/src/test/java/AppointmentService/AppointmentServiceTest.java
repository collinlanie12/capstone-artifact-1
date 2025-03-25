package AppointmentService;
import org.junit.jupiter.api.Test;

import java.util.Date;

import static org.junit.jupiter.api.Assertions.*;

public class AppointmentServiceTest {
    // Test adding an appointment
    @Test
    public void testAddAppointment() {
        // Create an appointmentService object
        AppointmentService appointmentService = new AppointmentService();
        // Create an appointment object
        Appointment appointment = new Appointment("001", new Date(System.currentTimeMillis() + 100000), "Appointment 1");

        // Test adding an appointment
        assertTrue(appointmentService.addAppointment(appointment)); // Should return true

        // Test adding an appointment that already exists
        assertFalse(appointmentService.addAppointment(appointment)); // Should return false
    }

    // Test deleting an appointment
    @Test
    public void testDeleteAppointment() {
        // Create an appointmentService object
        AppointmentService appointmentService = new AppointmentService();
        // Create an appointment object
        Appointment appointment = new Appointment("001", new Date(System.currentTimeMillis() + 100000), "Appointment 1");

        // Add the appointment object to the appointmentService object
        appointmentService.addAppointment(appointment);

        // Test deleting an appointment
        assertTrue(appointmentService.deleteAppointment("001")); // Should return true

        // Test deleting an appointment that does not exist
        assertFalse(appointmentService.deleteAppointment("001")); // Should return false
    }

}
