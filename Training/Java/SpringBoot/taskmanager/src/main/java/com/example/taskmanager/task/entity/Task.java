package com.example.taskmanager.task.entity;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.Instant;
import java.util.UUID;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class Task {

    private String id;
    private String title;
    private String description;
    private TaskStatus status;
    private TaskPriority priority;
    private String ownerId;       // references User.id
    private Instant createdAt;
    private Instant updatedAt;

    public static Task create(String title, String description, TaskPriority priority, String ownerId) {
        Instant now = Instant.now();
        return Task.builder()
                .id(UUID.randomUUID().toString())
                .title(title)
                .description(description)
                .status(TaskStatus.TODO)
                .priority(priority)
                .ownerId(ownerId)
                .createdAt(now)
                .updatedAt(now)
                .build();
    }

    public void markUpdated() {
        this.updatedAt = Instant.now();
    }
}
