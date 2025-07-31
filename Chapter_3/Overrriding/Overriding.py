class Person:
 
    def __init__(self, name):
        self.__name = name   
 
    @property
    def name(self):
        return self.__name
 
    def display_info(self):
        print(f"Name: {self.__name} ")
 
 
class Employee(Person):

    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

    def display_info(self):
        super().display_info()
        print(f"Company {self.company}")

    def work(self):
        print(f"{self.name} works {self.company}")

ted = Employee("Alpha", "VAZ")
ted.display_info()
ted.work()

