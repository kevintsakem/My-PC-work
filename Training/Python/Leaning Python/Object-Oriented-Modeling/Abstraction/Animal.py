from abc import ABC

class Animal(ABC):
    def __init__(self, pet_name, legs, tail):
        self.name = pet_name
        self.number_of_legs = legs
        self.number_of_tails = tail
        
    def walk(self):
        print(f"{self.name} is walking")
        
    def eat(self):
        print(f"{self.name} is eating")
        
    def run(self):
        print(f"{self.name} is running")

