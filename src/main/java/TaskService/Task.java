package TaskService;
public class Task {
    private final String taskID;
    private String name;
    private String description;

    public Task(String taskID, String name, String description) {
        // Validate input for null
//        if(taskID == null || name == null || description == null) {
//            throw new IllegalArgumentException("taskID, name, and description must not be null");
//        }
        if (taskID == null) {
            throw new IllegalArgumentException("taskID must not be null");
        }
        if (name == null) {
            throw new IllegalArgumentException("name must not be null");
        }
        if (description == null) {
            throw new IllegalArgumentException("description must not be null");
        }

        // Validate input for length
        if(taskID.length() > 10) {
            throw new IllegalArgumentException("taskID cannot be longer than 10 characters");
        }
        if(name.length() > 20) {
            throw new IllegalArgumentException("name cannot be longer than 20 characters");
        }
        if(description.length() > 50) {
            throw new IllegalArgumentException("description cannot be longer than 50 characters");
        }

        // Validate input for empty
        this.taskID = taskID;
        this.name = name;
        this.description = description;
    }

    public String getTaskID() {
        return taskID;
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public void setName(String name) {
        // Validate input for null
        if(name == null) {
            throw new IllegalArgumentException("name must not be null");
        }

        // Validate input for length
        if(name.length() > 20) {
            throw new IllegalArgumentException("name cannot be longer than 20 characters");
        }

        // Validate input for empty
        this.name = name;
    }

    public void setDescription(String description) {
        // Validate input for null
        if(description == null) {
            throw new IllegalArgumentException("description must not be null");
        }

        // Validate input for length
        if(description.length() > 50) {
            throw new IllegalArgumentException("description cannot be longer than 50 characters");
        }

        // Validate input for empty
        this.description = description;
    }
}

