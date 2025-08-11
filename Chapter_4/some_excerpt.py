try:
    number_1 = int(input("Enter a number_1: "))
    number_2 = int(input("Enter a number_2: "))

    print(number_1 / number_2)
except (ValueError, ZeroDivisionError):
    print("Некорректные данные и ли попытка деления на ноль")

print("\nEnd of the program")