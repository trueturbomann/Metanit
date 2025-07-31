class Employee:
    def works(self):
        print("Employee works")


class Student:
    def study(self):
        print("Student studies")

class Someone (Student, Employee):
    pass

someone = Someone()

#someone.works()
#someone.study()

class NewSomeone(Someone):
    pass

ns = NewSomeone()
ns.works()
ns.study()