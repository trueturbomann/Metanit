class Employee:
    def do(self):
        print("from Employee")

class Studend:
    def do(self):
        print("from Student")

# Будет вызван метод от класса первого в списке
class Someone(Studend,Employee):
    pass

someone = Someone()
someone.do()