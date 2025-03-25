package TaskService;
import java.util.HashMap;
import java.util.Map;
public class TaskService {
    private final Map<String, Task> tasks = new HashMap<>();

    public void addTask(Task task) {
        // validate if it already exists
        if(tasks.containsKey(task.getTaskID())) {
            throw new IllegalArgumentException("taskID already exists");
        }
        tasks.put(task.getTaskID(), task);
    }

    public void deleteTask(String taskID) {
        // validate if it exists
        if(!tasks.containsKey(taskID)) {
            throw new IllegalArgumentException("taskID does not exist");
        }
        tasks.remove(taskID);
    }

    public void updateTask(String taskID, String newName) {
        // validate if it exists
        if(!tasks.containsKey(taskID)) {
            throw new IllegalArgumentException("taskID does not exist");
        }
        Task task = tasks.get(taskID);
        task.setName(newName);
    }

    public void updateTaskDescription(String taskID, String newDescription) {
        // validate if it exists
        if(!tasks.containsKey(taskID)) {
            throw new IllegalArgumentException("taskID does not exist");
        }
        Task task = tasks.get(taskID);
        task.setDescription(newDescription);
    }

    public Task getTask(String taskID) {
        // validate if it exists
        if(!tasks.containsKey(taskID)) {
            throw new IllegalArgumentException("taskID does not exist");
        }
        return tasks.get(taskID);
    }
}
