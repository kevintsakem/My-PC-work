package com.example.bmi.DTO;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class BmiRequestDto {
    private String name;
    private double height;
    private double weight;
}
