class Person:
    def __init__(self, age, n):
        self.__age = age
        self.__name = n

    @property
    def age(self):
        return self.__age
    
    @age.setter    
    def age(self, age):
        if 0 < age < 110:
            self.__age = age
        else:
            print("Недопустимый возраст")


    @property
    def name(self):
       return self.__name


    @name.setter
    def name(self, n):
        self.__name = n

    

p = Person(34, "Toma")
print(p.age)
print(p.name)

p.age=134

print(p.age)
print(p.name)