class Employee:

    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    def works(self):
        print(f"{self.name} works")

class Student:

    def __init__(self, name):
        self.__name = name
    
    @property
    def name(self):
        return self.__name
    
    def study(self):
        print(f"{self.name} study")


class WorkandStudy(Employee, Student):
    pass

tom = WorkandStudy("Andy")
tom.study()
tom.works()