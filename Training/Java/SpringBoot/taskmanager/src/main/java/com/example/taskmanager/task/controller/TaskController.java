package com.example.taskmanager.task.controller;

import com.example.taskmanager.common.response.ApiResponse;
import com.example.taskmanager.task.dto.TaskDto.*;
import com.example.taskmanager.task.service.TaskService;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/tasks")
@RequiredArgsConstructor
public class TaskController {

    private final TaskService taskService;

    // Any authenticated user: creates task for themselves
    @PostMapping
    public ResponseEntity<ApiResponse<TaskResponse>> createTask(
            @Valid @RequestBody CreateTaskRequest request,
            @AuthenticationPrincipal UserDetails currentUser
    ) {
        TaskResponse task = taskService.createTask(request, currentUser.getUsername());
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(ApiResponse.success(task, "Task created"));
    }

    // ADMIN → all tasks | USER → own tasks (data-level filter in service)
    @GetMapping
    public ResponseEntity<ApiResponse<List<TaskResponse>>> getTasks(
            @AuthenticationPrincipal UserDetails currentUser
    ) {
        return ResponseEntity.ok(ApiResponse.success(taskService.getTasks(currentUser.getUsername())));
    }

    // ADMIN → any task | USER → own task only
    @GetMapping("/{id}")
    public ResponseEntity<ApiResponse<TaskResponse>> getTaskById(
            @PathVariable String id,
            @AuthenticationPrincipal UserDetails currentUser
    ) {
        return ResponseEntity.ok(ApiResponse.success(taskService.getTaskById(id, currentUser.getUsername())));
    }

    // ADMIN → any task | USER → own task only
    @PutMapping("/{id}")
    public ResponseEntity<ApiResponse<TaskResponse>> updateTask(
            @PathVariable String id,
            @RequestBody UpdateTaskRequest request,
            @AuthenticationPrincipal UserDetails currentUser
    ) {
        return ResponseEntity.ok(ApiResponse.success(taskService.updateTask(id, request, currentUser.getUsername())));
    }

    // ADMIN only: reassign task to another user
    @PatchMapping("/{id}/assign")
    @PreAuthorize("hasRole('ADMIN')")
    public ResponseEntity<ApiResponse<TaskResponse>> assignTask(
            @PathVariable String id,
            @Valid @RequestBody AssignTaskRequest request
    ) {
        return ResponseEntity.ok(ApiResponse.success(taskService.assignTask(id, request), "Task assigned"));
    }

    // ADMIN → any task | USER → own task only
    @DeleteMapping("/{id}")
    public ResponseEntity<ApiResponse<Void>> deleteTask(
            @PathVariable String id,
            @AuthenticationPrincipal UserDetails currentUser
    ) {
        taskService.deleteTask(id, currentUser.getUsername());
        return ResponseEntity.ok(ApiResponse.success(null, "Task deleted"));
    }
}
