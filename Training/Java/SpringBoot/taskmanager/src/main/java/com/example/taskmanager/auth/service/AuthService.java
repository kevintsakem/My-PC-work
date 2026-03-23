package com.example.taskmanager.auth.service;

import com.example.taskmanager.auth.dto.AuthDto.*;
import com.example.taskmanager.auth.repository.RefreshTokenRepository;
import com.example.taskmanager.common.exception.BadRequestException;
import com.example.taskmanager.security.jwt.JwtService;
import com.example.taskmanager.user.entity.Role;
import com.example.taskmanager.user.entity.User;
import com.example.taskmanager.user.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
public class AuthService {

    private final UserService userService;
    private final JwtService jwtService;
    private final PasswordEncoder passwordEncoder;
    private final AuthenticationManager authenticationManager;
    private final UserDetailsService userDetailsService;
    private final RefreshTokenRepository refreshTokenRepository;

    public AuthResponse register(RegisterRequest request) {
        if (userService.emailExists(request.email())) {
            throw new BadRequestException("Email already registered: " + request.email());
        }

        User user = User.create(
                request.username(),
                request.email(),
                passwordEncoder.encode(request.password()),
                Role.ROLE_USER  // default role on registration
        );
        userService.saveUser(user);

        UserDetails userDetails = userDetailsService.loadUserByUsername(user.getEmail());
        String accessToken = jwtService.generateAccessToken(userDetails);
        String refreshToken = jwtService.generateRefreshToken(userDetails);

        refreshTokenRepository.save(user.getId(), refreshToken);

        return AuthResponse.of(accessToken, refreshToken, user.getEmail(), user.getRole().name());
    }

    public AuthResponse login(LoginRequest request) {
        // Delegates to CustomAuthenticationProvider — throws on bad credentials
        authenticationManager.authenticate(
                new UsernamePasswordAuthenticationToken(request.email(), request.password())
        );

        User user = userService.findUserByEmail(request.email());
        UserDetails userDetails = userDetailsService.loadUserByUsername(user.getEmail());

        String accessToken = jwtService.generateAccessToken(userDetails);
        String refreshToken = jwtService.generateRefreshToken(userDetails);

        // Rotate refresh token on each login
        refreshTokenRepository.save(user.getId(), refreshToken);

        return AuthResponse.of(accessToken, refreshToken, user.getEmail(), user.getRole().name());
    }

    public AuthResponse refresh(RefreshTokenRequest request) {
        String incomingToken = request.refreshToken();

        // 1. Token must exist in our store (wasn't logged out / revoked)
        if (!refreshTokenRepository.exists(incomingToken)) {
            throw new BadRequestException("Refresh token not recognized or already revoked");
        }

        // 2. Extract username and load user
        String email = jwtService.extractUsername(incomingToken);
        UserDetails userDetails = userDetailsService.loadUserByUsername(email);

        // 3. Validate token signature, expiry, and type
        if (!jwtService.isRefreshTokenValid(incomingToken, userDetails)) {
            refreshTokenRepository.deleteByToken(incomingToken);
            throw new BadRequestException("Refresh token is expired or invalid");
        }

        User user = userService.findUserByEmail(email);

        // 4. Issue new token pair (refresh token rotation)
        String newAccessToken = jwtService.generateAccessToken(userDetails);
        String newRefreshToken = jwtService.generateRefreshToken(userDetails);

        refreshTokenRepository.save(user.getId(), newRefreshToken);

        return AuthResponse.of(newAccessToken, newRefreshToken, user.getEmail(), user.getRole().name());
    }

    public void logout(String refreshToken) {
        refreshTokenRepository.deleteByToken(refreshToken);
    }
}
