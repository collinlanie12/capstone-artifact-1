package AppointmentService;
import java.util.HashMap;
import java.util.Map;

public class AppointmentService {
    // Map to store appointments by ID
    private final Map<String, Appointment> appointments = new HashMap<>();

    // Method to add an appointment
    public boolean addAppointment(Appointment appointment) {
        // Validate if appointment already exists
        if(appointments.containsKey(appointment.getAppointmentId())) {
            return false; // Appointment already exists return false
        }
        appointments.put(appointment.getAppointmentId(), appointment);
        return true; // Appointment added successfully return true
    }

    // Method to delete an appointment
    public boolean deleteAppointment(String appointmentId) {
        // Validate if appointment exists
        if(!appointments.containsKey(appointmentId)) {
            return false; // Appointment does not exist return false
        }
        appointments.remove(appointmentId);
        return true; // Appointment deleted successfully return true
    }

}
