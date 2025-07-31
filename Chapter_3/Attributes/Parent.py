class Parent:
    default_name = "Undefine"

    def __init__(self, name):
        if name: 
            self.name = name
        else:
            self.name = Parent.default_name
 
tom = Parent("Tom")
rom = Parent("")

print(tom.name)
print(rom.name)