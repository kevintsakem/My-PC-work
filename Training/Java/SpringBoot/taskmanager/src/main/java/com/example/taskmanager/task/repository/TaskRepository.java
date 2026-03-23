package com.example.taskmanager.task.repository;

import com.example.taskmanager.task.entity.Task;
import org.springframework.stereotype.Repository;

import java.util.Collection;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

/**
 * In-memory task store.
 * Keyed by taskId. Owner filtering is done at query time.
 */
@Repository
public class TaskRepository {

    private final Map<String, Task> store = new ConcurrentHashMap<>();

    public Task save(Task task) {
        store.put(task.getId(), task);
        return task;
    }

    public Optional<Task> findById(String id) {
        return Optional.ofNullable(store.get(id));
    }

    public Collection<Task> findAll() {
        return store.values();
    }

    public List<Task> findByOwnerId(String ownerId) {
        return store.values().stream()
                .filter(t -> t.getOwnerId().equals(ownerId))
                .toList();
    }

    public void deleteById(String id) {
        store.remove(id);
    }

    public boolean existsById(String id) {
        return store.containsKey(id);
    }
}
