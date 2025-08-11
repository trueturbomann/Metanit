try:
    number_1 = int(input("Enter a number_1: \n"))
    number_2 = int(input("Enter a number_2: \n"))

    print("Divide number_1 on number_2 = ", number_1 / number_2)

except ZeroDivisionError:
    print("Divide by zero")

print("End of the program")