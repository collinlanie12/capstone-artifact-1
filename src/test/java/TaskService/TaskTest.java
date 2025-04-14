package TaskService;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TaskTest {

    @Test
    public void testCreateTask() {
        // Create a task object
        Task task = new Task("05003", "Task 101", "Description 101");
        // Check if the taskID is equal to "05003"
        assertEquals("05003", task.getTaskID());
        // Check if the name is equal to "Task 101"
        assertEquals("Task 101", task.getName());
        // Check if the description is equal to "Description 101"
        assertEquals("Description 101", task.getDescription());
    }

    @Test
    public void testInvalidTaskID() {
        // Create a task object with an invalid taskID
        try {
            Task task = new Task("50000000000000", "Task 101", "Description 101");
        } catch (IllegalArgumentException e) {
            assertEquals("taskID cannot be longer than 10 characters", e.getMessage());
        }
    }

    @Test
    public void testInvalidName() {
        try {
            // Create a task object with an invalid name
            Task task = new Task("05003", "Task 101 Task 101 Task 101", "Description 101");
        } catch (IllegalArgumentException e) {
            assertEquals("name cannot be longer than 20 characters", e.getMessage());
        }
    }

    @Test
    public void testInvalidDescription() {
        try {
            // Create a task object with an invalid description
            Task task = new Task("05003", "Task 101", "Description 101 Description 101 Description 101 Description 101 Description 101");
        } catch (IllegalArgumentException e) {
            assertEquals("description cannot be longer than 50 characters", e.getMessage());
        }
    }

    @Test
    public void testUpdateName() {
        // Create a task object
        Task task = new Task("05003", "Task 101", "Description 101");
        // Update the name of the task object
        task.setName("Task 102");
        // Check if the name of the task object is equal to "Task 102"
        assertEquals("Task 102", task.getName());
    }

    @Test
    public void testUpdateDescription() {
        // Create a task object
        Task task = new Task("05003", "Task 101", "Description 101");
        // Update the description of the task object
        task.setDescription("Description 102");
        // Check if the description of the task object is equal to "Description 102"
        assertEquals("Description 102", task.getDescription());
    }

    @Test
    public void testNullTaskID() {
        try {
            // Create a task object with a null taskID
            Task task = new Task(null, "Task 101", "Description 101");
        } catch (IllegalArgumentException e) {
            assertEquals("taskID must not be null", e.getMessage());
        }
    }

    @Test
    public void testNullName() {
        try {
            // Create a task object with a null name
            Task task = new Task("05003", null, "Description 101");
        } catch (IllegalArgumentException e) {
            assertEquals("name must not be null", e.getMessage());
        }
    }

    @Test
    public void testNullDescription() {
        try {
            // Create a task object with a null description
            Task task = new Task("05003", "Task 101", null);
        } catch (IllegalArgumentException e) {
            assertEquals("description must not be null", e.getMessage());
        }
    }
}
