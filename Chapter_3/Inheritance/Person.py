class Person:
 
    def __init__(self, name):
        self.__name = name 
 
    @property
    def name(self):
        return self.__name
     
    def display_info(self):
        print(f"Name: {self.__name} ")




class Employee(Person):
    
    def works(self):
        print(f"{self.name} works")


tom = Employee("Tom")
print(tom.name)

tom.display_info()
tom.works()
        