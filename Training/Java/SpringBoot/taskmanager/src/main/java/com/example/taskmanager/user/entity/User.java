package com.example.taskmanager.user.entity;

import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.UUID;

@Data
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class User {

    private String id;
    private String username;
    private String email;
    private String password;
    private Role role;

    public static User create(String username, String email, String password, Role role) {
        return User.builder()
                .id(UUID.randomUUID().toString())
                .username(username)
                .email(email)
                .password(password)
                .role(role)
                .build();
    }
}
