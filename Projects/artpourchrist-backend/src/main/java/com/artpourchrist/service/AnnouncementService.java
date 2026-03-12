package com.artpourchrist.service;

import com.artpourchrist.dto.AnnouncementDto;
import com.artpourchrist.model.Activity;
import com.artpourchrist.model.Announcement;
import com.artpourchrist.repository.AnnouncementRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@RequiredArgsConstructor
public class AnnouncementService {

    private final AnnouncementRepository repository;
    private final ActivityService activityService;

    public List<AnnouncementDto.Response> getAll() {
        return repository.findAllByOrderByCreatedAtDesc()
                .stream().map(this::toResponse).toList();
    }

    public AnnouncementDto.Response getById(String id) {
        return toResponse(findById(id));
    }

    public AnnouncementDto.Response create(AnnouncementDto.Request req) {
        Announcement announcement = Announcement.builder()
                .title(req.getTitle())
                .description(req.getDescription())
                .date(req.getDate())
                .time(req.getTime())
                .location(req.getLocation())
                .category(req.getCategory())
                .featured(req.isFeatured())
                .build();

        announcement = repository.save(announcement);
        activityService.log(announcement.getTitle(), Activity.ActivityType.announcement, Activity.ActivityAction.created);
        return toResponse(announcement);
    }

    public AnnouncementDto.Response update(String id, AnnouncementDto.Request req) {
        Announcement announcement = findById(id);
        announcement.setTitle(req.getTitle());
        announcement.setDescription(req.getDescription());
        announcement.setDate(req.getDate());
        announcement.setTime(req.getTime());
        announcement.setLocation(req.getLocation());
        announcement.setCategory(req.getCategory());
        announcement.setFeatured(req.isFeatured());

        announcement = repository.save(announcement);
        activityService.log(announcement.getTitle(), Activity.ActivityType.announcement, Activity.ActivityAction.updated);
        return toResponse(announcement);
    }

    public void delete(String id) {
        Announcement announcement = findById(id);
        activityService.log(announcement.getTitle(), Activity.ActivityType.announcement, Activity.ActivityAction.deleted);
        repository.deleteById(id);
    }

    private Announcement findById(String id) {
        return repository.findById(id)
                .orElseThrow(() -> new RuntimeException("Annonce non trouvée: " + id));
    }

    private AnnouncementDto.Response toResponse(Announcement a) {
        return AnnouncementDto.Response.builder()
                .id(a.getId())
                .title(a.getTitle())
                .description(a.getDescription())
                .date(a.getDate())
                .time(a.getTime())
                .location(a.getLocation())
                .category(a.getCategory())
                .featured(a.isFeatured())
                .createdAt(a.getCreatedAt() != null ? a.getCreatedAt().toString() : null)
                .build();
    }
}
