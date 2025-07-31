class Person:
    __type = "Person"

    @staticmethod
    def print_type():
        print(Person.__type)

print("Вызываем статический метод")
Person.print_type()


print("Вызываем статический метод у эеземпляра")

tom = Person()
tom.print_type()