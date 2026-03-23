package com.example.taskmanager.task.service;

import com.example.taskmanager.common.exception.ForbiddenException;
import com.example.taskmanager.common.exception.ResourceNotFoundException;
import com.example.taskmanager.task.dto.TaskDto.*;
import com.example.taskmanager.task.entity.Task;
import com.example.taskmanager.task.repository.TaskRepository;
import com.example.taskmanager.user.entity.Role;
import com.example.taskmanager.user.entity.User;
import com.example.taskmanager.user.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class TaskService {

    private final TaskRepository taskRepository;
    private final UserService userService;

    // ─── Create ──────────────────────────────────────────────────────────────

    public TaskResponse createTask(CreateTaskRequest request, String ownerEmail) {
        User owner = userService.findUserByEmail(ownerEmail);
        Task task = Task.create(request.title(), request.description(), request.priority(), owner.getId());
        return TaskResponse.from(taskRepository.save(task));
    }

    // ─── Read ────────────────────────────────────────────────────────────────

    /**
     * ADMIN → all tasks.
     * USER  → only their own tasks.
     */
    public List<TaskResponse> getTasks(String requesterEmail) {
        User requester = userService.findUserByEmail(requesterEmail);

        if (requester.getRole() == Role.ROLE_ADMIN) {
            return taskRepository.findAll().stream()
                    .map(TaskResponse::from)
                    .toList();
        }

        return taskRepository.findByOwnerId(requester.getId()).stream()
                .map(TaskResponse::from)
                .toList();
    }

    public TaskResponse getTaskById(String taskId, String requesterEmail) {
        Task task = findTaskOrThrow(taskId);
        assertCanAccess(task, requesterEmail);
        return TaskResponse.from(task);
    }

    // ─── Update ──────────────────────────────────────────────────────────────

    public TaskResponse updateTask(String taskId, UpdateTaskRequest request, String requesterEmail) {
        Task task = findTaskOrThrow(taskId);
        assertCanAccess(task, requesterEmail);

        if (request.title() != null)       task.setTitle(request.title());
        if (request.description() != null) task.setDescription(request.description());
        if (request.status() != null)      task.setStatus(request.status());
        if (request.priority() != null)    task.setPriority(request.priority());
        task.markUpdated();

        return TaskResponse.from(taskRepository.save(task));
    }

    // ─── Assign (Admin only) ─────────────────────────────────────────────────

    /**
     * Reassigns a task to another user. Admin-only — enforced at controller level via @PreAuthorize.
     */
    public TaskResponse assignTask(String taskId, AssignTaskRequest request) {
        Task task = findTaskOrThrow(taskId);

        // Verify the target user exists (throws ResourceNotFoundException if not)
        userService.getUserById(request.userId());

        task.setOwnerId(request.userId());
        task.markUpdated();
        return TaskResponse.from(taskRepository.save(task));
    }

    // ─── Delete ──────────────────────────────────────────────────────────────

    public void deleteTask(String taskId, String requesterEmail) {
        Task task = findTaskOrThrow(taskId);
        assertCanAccess(task, requesterEmail);
        taskRepository.deleteById(taskId);
    }

    // ─── Helpers ─────────────────────────────────────────────────────────────

    private Task findTaskOrThrow(String taskId) {
        return taskRepository.findById(taskId)
                .orElseThrow(() -> new ResourceNotFoundException("Task not found with id: " + taskId));
    }

    /**
     * Data-level access check:
     * - ADMIN can access any task
     * - USER can only access tasks they own
     */
    private void assertCanAccess(Task task, String requesterEmail) {
        User requester = userService.findUserByEmail(requesterEmail);
        if (requester.getRole() == Role.ROLE_ADMIN) return;
        if (!task.getOwnerId().equals(requester.getId())) {
            throw new ForbiddenException("You do not have permission to access this task");
        }
    }
}
