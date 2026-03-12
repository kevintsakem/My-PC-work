
class Lion:
    
    def __init__(self,name,leg,age):
        self.__name = name
        self.__leg = leg
        self.__age = age
    
    @property
    def get_name(self):
        return self.__name
    
    @property
    def get_age(self):
        return self.__age
    
    @property
    def get_leg(self):
        return self.__leg
    
    @get_name.setter
    def set_name(self,name):
        self.__name = name
        
    @get_age.setter
    def set_age(self,age):
        if(age > 0):
            self.__age = age
        else:
            print("Enter a valid age")
    
    @get_leg.setter
    def set_leg(self,leg):
        if(leg > 1):
            self.__leg = leg
        else:
            print("Enter a valid number")
    
    
    