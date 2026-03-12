from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def run(self):
        pass
    
    @abstractmethod
    def speak(self):
        pass
    