package com.example.bmi.Controller;

import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.bmi.DTO.BmiRequestDto;
import com.example.bmi.DTO.BmiResponseDTO;
import com.example.bmi.Service.BmiService;

import lombok.AllArgsConstructor;
import lombok.Data;

@Data
@AllArgsConstructor
@RestController
@RequestMapping("/bmi")
class BmiController {

    public final BmiService bmi_service;

    @PostMapping
    public BmiResponseDTO controller(@RequestBody BmiRequestDto donnees_utilisateur){
        return bmi_service.calculate(donnees_utilisateur);
    }
}