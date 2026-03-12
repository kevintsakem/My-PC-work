package com.example.bmi.DTO;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class BmiResponseDTO {
    private String name;
    private double bmi;
    private String category;
}
