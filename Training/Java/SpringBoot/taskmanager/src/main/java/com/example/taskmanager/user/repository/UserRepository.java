package com.example.taskmanager.user.repository;

import com.example.taskmanager.user.entity.User;
import org.springframework.stereotype.Repository;

import java.util.Collection;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

/**
 * In-memory user store using ConcurrentHashMap for thread safety.
 * Keyed by userId for fast lookup; secondary index by email.
 */
@Repository
public class UserRepository {

    private final Map<String, User> usersById = new ConcurrentHashMap<>();
    private final Map<String, String> emailToId = new ConcurrentHashMap<>();

    public User save(User user) {
        usersById.put(user.getId(), user);
        emailToId.put(user.getEmail().toLowerCase(), user.getId());
        return user;
    }

    public Optional<User> findById(String id) {
        return Optional.ofNullable(usersById.get(id));
    }

    public Optional<User> findByEmail(String email) {
        String id = emailToId.get(email.toLowerCase());
        return Optional.ofNullable(id).map(usersById::get);
    }

    public boolean existsByEmail(String email) {
        return emailToId.containsKey(email.toLowerCase());
    }

    public Collection<User> findAll() {
        return usersById.values();
    }

    public void deleteById(String id) {
        User user = usersById.remove(id);
        if (user != null) {
            emailToId.remove(user.getEmail().toLowerCase());
        }
    }
}
