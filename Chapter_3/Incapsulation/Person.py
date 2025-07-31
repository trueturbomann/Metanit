class Person:
    def __init__(self,  a, n):
        self.__age = a
        self.__name = n

    def say(self):
        print (f"My name is: {self.__name} I'm {self.__age} old "  )

p = Person(44, "Eduard")
p.age = 11

print(p.age)
p.say()