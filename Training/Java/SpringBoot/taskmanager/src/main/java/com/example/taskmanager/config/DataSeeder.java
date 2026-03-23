package com.example.taskmanager.config;

import com.example.taskmanager.user.entity.Role;
import com.example.taskmanager.user.entity.User;
import com.example.taskmanager.user.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.boot.CommandLineRunner;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

/**
 * Seeds an admin user on startup so the app is immediately usable.
 * In production this would be replaced by a proper bootstrap mechanism.
 */
@Slf4j
@Component
@RequiredArgsConstructor
public class DataSeeder implements CommandLineRunner {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;

    @Override
    public void run(String... args) {
        if (!userRepository.existsByEmail("admin@example.com")) {
            User admin = User.create(
                    "admin",
                    "admin@example.com",
                    passwordEncoder.encode("admin123"),
                    Role.ROLE_ADMIN
            );
            userRepository.save(admin);
            log.info("✅ Admin user seeded → email: admin@example.com | password: admin123");
        }
    }
}
