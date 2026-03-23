package com.example.taskmanager.user.dto;

import com.example.taskmanager.user.entity.Role;
import com.example.taskmanager.user.entity.User;

public class UserDto {

    public record UserResponse(
            String id,
            String username,
            String email,
            Role role
    ) {
        public static UserResponse from(User user) {
            return new UserResponse(user.getId(), user.getUsername(), user.getEmail(), user.getRole());
        }
    }
}
