package com.example.bmi;

import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

import com.example.bmi.Entity.Person;
import com.example.bmi.Repository.PersonsRepository;

@SpringBootApplication
public class BmiApplication {

	public static void main(String[] args) {
		SpringApplication.run(BmiApplication.class, args);
	}

	@Bean
	CommandLineRunner runner (PersonsRepository repo){
		return args-> {
			Person p = new Person();
			p.setName("Jack");
			p.setHeight(1.75);
			p.setWeight(75);

			repo.save(p);

			System.out.println("Initial Database Seeded ");
		};
	}
}
