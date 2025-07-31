class Person:
    name = "Undefined"

    def print_name(self):
        print(self.name)


tom = Person()
rom = Person()

print("До установки имени")

tom.print_name()
rom.print_name()

print("Установим имя")

tom.name = "Tom"

tom.print_name()
rom.print_name()

print("Установим значение атрибута класса")

Person.name = "NEW NAME"

tom.print_name()
rom.print_name()