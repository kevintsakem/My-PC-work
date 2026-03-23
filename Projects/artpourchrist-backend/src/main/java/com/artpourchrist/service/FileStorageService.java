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
import java.util.Set;
import java.util.UUID;

@Slf4j
@Service
public class FileStorageService {

    private static final Set<String> ALLOWED_IMAGE_TYPES = Set.of(
            "image/jpeg", "image/png", "image/webp", "image/gif"
    );
    private static final Set<String> ALLOWED_VIDEO_TYPES = Set.of(
            "video/mp4", "video/webm", "video/ogg", "video/quicktime"
    );
    private static final Set<String> ALLOWED_THUMBNAIL_TYPES = Set.of(
            "image/jpeg", "image/png", "image/webp"
    );

    @Value("${app.upload.dir}")
    private String uploadDir;

    @Value("${app.base-url}")
    private String baseUrl;

    public String storeImage(MultipartFile file, String subfolder) {
        validateContentType(file, ALLOWED_IMAGE_TYPES);
        return store(file, subfolder);
    }

    public String storeVideo(MultipartFile file, String subfolder) {
        validateContentType(file, ALLOWED_VIDEO_TYPES);
        return store(file, subfolder);
    }

    public String storeThumbnail(MultipartFile file, String subfolder) {
        validateContentType(file, ALLOWED_THUMBNAIL_TYPES);
        return store(file, subfolder);
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

    private void validateContentType(MultipartFile file, Set<String> allowedTypes) {
        String contentType = file.getContentType();
        if (contentType == null || !allowedTypes.contains(contentType)) {
            throw new RuntimeException(
                    "Type de fichier non autorisé: " + contentType +
                    ". Types acceptés: " + allowedTypes
            );
        }
    }

    private String store(MultipartFile file, String subfolder) {
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

    private String getExtension(String filename) {
        if (filename == null || !filename.contains(".")) return "";
        return filename.substring(filename.lastIndexOf(".")).toLowerCase();
    }
}
