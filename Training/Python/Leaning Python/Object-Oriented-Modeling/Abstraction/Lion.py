from Animal import Animal

class Lion(Animal):
    def __init__(self, name, legs, tails):
        super().__init__(name,legs,tails)


    def roar(self):
        print(f"{self.name} is roaring")
    