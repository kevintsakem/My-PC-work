package com.example.bmi.Service;

import org.springframework.stereotype.Service;

import com.example.bmi.DTO.BmiRequestDto;
import com.example.bmi.DTO.BmiResponseDTO;
import com.example.bmi.Entity.Person;
import com.example.bmi.Repository.PersonsRepository;

import lombok.AllArgsConstructor;
import lombok.Data;


@Service
@Data
@AllArgsConstructor
public class BmiService {

    private final PersonsRepository repo;

    public BmiResponseDTO calculate (BmiRequestDto request){
        double bmi = request.getWeight()/(request.getHeight()*request.getHeight());

        String category;

        if (bmi < 18.5)
            category = "Underweight";
        else if (bmi < 25)
            category = "Normal";
        else if (bmi < 30)
            category = "Overweight";
        else
            category = "Obese";


        Person person = new Person();

        person.setName(request.getName());
        person.setWeight(request.getWeight());
        person.setHeight(request.getHeight());
        person.setBmi(bmi);
        return new BmiResponseDTO(request.getName(), bmi, category);       
    }


}
