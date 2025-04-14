package AppointmentService;
import java.util.Date;

public class Appointment {
    private final String appointmentId;
    private final Date appointmentDate;
    private final String description;

    public Appointment(String appointmentId, Date appointmentDate, String description) {
        // Appointment ID cannot be null and must be less than 10 characters
        if (appointmentId == null || appointmentId.length() > 10) {
            throw new IllegalArgumentException("Appointment ID invalid");
        }
        // Appointment date cannot be null and cannot be in the past
        if (appointmentDate == null || appointmentDate.before(new Date())) {
            throw new IllegalArgumentException("Appointment date invalid");
        }
        // Description cannot be null and must be less than 50 characters
        if (description == null || description.length() > 50) {
            throw new IllegalArgumentException("Description invalid");
        }

        // Initialization of the fields
        this.appointmentId = appointmentId;
        this.appointmentDate = appointmentDate;
        this.description = description;
    }

    // Getters
    public String getAppointmentId() {
        return appointmentId;
    }

    public Date getAppointmentDate() {
        return appointmentDate;
    }

    public String getDescription() {
        return description;
    }
}
