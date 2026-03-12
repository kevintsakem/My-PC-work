package com.example.bmi.Repository;

import org.springframework.data.jpa.repository.JpaRepository;

import com.example.bmi.Entity.Person;

public interface PersonsRepository extends JpaRepository<Person, Long>{
    
}

