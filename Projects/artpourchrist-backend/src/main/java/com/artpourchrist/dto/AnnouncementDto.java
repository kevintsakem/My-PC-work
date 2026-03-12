package com.artpourchrist.dto;

import jakarta.validation.constraints.NotBlank;
import lombok.Data;
import lombok.Builder;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

public class AnnouncementDto {

    @Data
    public static class Request {
        @NotBlank(message = "Titre requis")
        private String title;

        @NotBlank(message = "Description requise")
        private String description;

        @NotBlank(message = "Date requise")
        private String date;

        private String time;
        private String location;

        @NotBlank(message = "Catégorie requise")
        private String category;

        private boolean featured = false;
    }

    @Data
    @Builder
    @NoArgsConstructor
    @AllArgsConstructor
    public static class Response {
        private String id;
        private String title;
        private String description;
        private String date;
        private String time;
        private String location;
        private String category;
        private boolean featured;
        private String createdAt;
    }
}
