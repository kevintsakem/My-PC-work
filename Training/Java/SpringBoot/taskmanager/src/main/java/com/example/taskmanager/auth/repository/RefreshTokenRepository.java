package com.example.taskmanager.auth.repository;

import org.springframework.stereotype.Repository;

import java.util.Map;
import java.util.Optional;
import java.util.concurrent.ConcurrentHashMap;

/**
 * In-memory refresh token store.
 * Maps userId → refreshToken (one active refresh token per user).
 *
 * In production this would be a Redis cache with TTL set to
 * the refresh token expiration time.
 */
@Repository
public class RefreshTokenRepository {

    // userId → refreshToken
    private final Map<String, String> store = new ConcurrentHashMap<>();
    // refreshToken → userId (reverse index for fast lookup)
    private final Map<String, String> reverseStore = new ConcurrentHashMap<>();

    public void save(String userId, String refreshToken) {
        // Invalidate any previous token for this user
        String old = store.get(userId);
        if (old != null) reverseStore.remove(old);

        store.put(userId, refreshToken);
        reverseStore.put(refreshToken, userId);
    }

    public Optional<String> findUserIdByToken(String refreshToken) {
        return Optional.ofNullable(reverseStore.get(refreshToken));
    }

    public Optional<String> findTokenByUserId(String userId) {
        return Optional.ofNullable(store.get(userId));
    }

    public void deleteByUserId(String userId) {
        String token = store.remove(userId);
        if (token != null) reverseStore.remove(token);
    }

    public void deleteByToken(String refreshToken) {
        String userId = reverseStore.remove(refreshToken);
        if (userId != null) store.remove(userId);
    }

    public boolean exists(String refreshToken) {
        return reverseStore.containsKey(refreshToken);
    }
}
