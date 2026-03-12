package com.artpourchrist.service;

import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.UUID;

@Slf4j
@Service
public class FileStorageService {

    @Value("${app.upload.dir}")
    private String uploadDir;

    @Value("${app.base-url}")
    private String baseUrl;

    public String store(MultipartFile file, String subfolder) {
        try {
            Path directory = Paths.get(uploadDir, subfolder).toAbsolutePath();
            Files.createDirectories(directory);

            String extension = getExtension(file.getOriginalFilename());
            String filename = UUID.randomUUID() + extension;
            Path destination = directory.resolve(filename);

            Files.copy(file.getInputStream(), destination, StandardCopyOption.REPLACE_EXISTING);

            return subfolder + "/" + filename;
        } catch (IOException e) {
            throw new RuntimeException("Impossible de stocker le fichier: " + e.getMessage(), e);
        }
    }

    public String getUrl(String relativePath) {
        return baseUrl + "/uploads/" + relativePath;
    }

    public void delete(String relativePath) {
        if (relativePath == null) return;
        try {
            Path file = Paths.get(uploadDir, relativePath).toAbsolutePath();
            Files.deleteIfExists(file);
        } catch (IOException e) {
            log.warn("Impossible de supprimer le fichier: {}", relativePath);
        }
    }

    private String getExtension(String filename) {
        if (filename == null || !filename.contains(".")) return "";
        return filename.substring(filename.lastIndexOf("."));
    }
}
