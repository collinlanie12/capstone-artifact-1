package TaskService;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TaskServiceTest {

    @Test
    public void testAddTask() {
        // Create a taskService object
        TaskService taskService = new TaskService();
        // Create a task object
        Task task = new Task("05003", "Task 101", "Description 101");
        // Add the task object to the taskService object
        taskService.addTask(task);
        // Check if the taskID is equal to "05003"
        assertEquals("05003", taskService.getTask("05003").getTaskID());
    }

    @Test
    public void testDeleteTask() {
        // Create a taskService object
        TaskService taskService = new TaskService();
        // Create a task object
        Task task = new Task("05003", "Task 101", "Description 101");
        // Add the task object to the taskService object
        taskService.addTask(task);
        // Delete the task object from the taskService object
        taskService.deleteTask("05003");
        try {
            // Try to get the task object from the taskService object
            taskService.getTask("05003");
        } catch (IllegalArgumentException e) {
            assertEquals("taskID does not exist", e.getMessage());
        }
    }

    @Test
    public void testUpdateName() {
        // Create a taskService object
        TaskService taskService = new TaskService();
        // Create a task object
        Task task = new Task("05003", "Task 101", "Description 101");
        taskService.addTask(task);
        // Update the name of the task object
        taskService.updateTask("05003", "Task 102");
        // Check if the name of the task object is equal to "Task 102"
        assertEquals("Task 102", taskService.getTask("05003").getName());
    }

    @Test
    public void testUpdateDescription() {
        // Create a taskService object
        TaskService taskService = new TaskService();
        // Create a task object
        Task task = new Task("05003", "Task 101", "Description 101");
        // Add the task object to the taskService object
        taskService.addTask(task);
        // Update the description of the task object
        taskService.updateTaskDescription("05003", "Description 102");
        // Check if the description of the task object is equal to "Description 102"
        assertEquals("Description 102", taskService.getTask("05003").getDescription());
    }
}
