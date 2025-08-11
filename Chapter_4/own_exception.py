class PersonAgeException(Exception):
    def __init__(self, age,name, minage, maxage):
        self.age = age
        self.name = name
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f" Wrong age: {self.age}" \
                f"\nAge should be between {self.minage} and {self.maxage}"

class Person:
    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 120
        if minage < age < maxage:
            self.__age = age
        else:
            raise PersonAgeException(name, age, minage, maxage)

    def display_info(self):
        print (f"Name: {self.__name}, age: {self.__age}")


try:
    rom = Person("Rom", 38)
    rom.display_info()

    bob = Person("Bob", -22)
    bob.display_info()
except PersonAgeException as e:
    print(e)

