class Person:
    type = "Person"
    description = "this is a person"



print(Person.type)
print(Person.description)

print("=======")
Person.type = "New Type"
print(Person.type)


