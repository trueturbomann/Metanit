try:
    print("Введите число")
    n = int(input())
    print("Вы ввели", n )
except:
    print("Вы ввели не число")
finally:
    print("Блок кода будет выполнен независимо")

