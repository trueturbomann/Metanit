class Person:

    type = "Person"

    def __init__(self, name):
        self.name = name


tom = Person("Tom")
rom = Person("Rom")

print(tom.type)
print(rom.type)

print("------------")

Person.type = "NEW TYPE"


print(tom.type)
print(rom.type)