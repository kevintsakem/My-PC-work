package com.example.taskmanager.task.dto;

import com.example.taskmanager.task.entity.Task;
import com.example.taskmanager.task.entity.TaskPriority;
import com.example.taskmanager.task.entity.TaskStatus;
import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;

import java.time.Instant;

public class TaskDto {

    public record CreateTaskRequest(
            @NotBlank(message = "Title is required")
            String title,

            String description,

            @NotNull(message = "Priority is required")
            TaskPriority priority
    ) {}

    public record UpdateTaskRequest(
            String title,
            String description,
            TaskStatus status,
            TaskPriority priority
    ) {}

    public record AssignTaskRequest(
            @NotBlank(message = "Target user ID is required")
            String userId
    ) {}

    public record TaskResponse(
            String id,
            String title,
            String description,
            TaskStatus status,
            TaskPriority priority,
            String ownerId,
            Instant createdAt,
            Instant updatedAt
    ) {
        public static TaskResponse from(Task task) {
            return new TaskResponse(
                    task.getId(),
                    task.getTitle(),
                    task.getDescription(),
                    task.getStatus(),
                    task.getPriority(),
                    task.getOwnerId(),
                    task.getCreatedAt(),
                    task.getUpdatedAt()
            );
        }
    }
}
