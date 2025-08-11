try:
    number_1 = int(input("Enter number_1\n"))
    number_2 = int(input("Enter number_2\n"))
    print("Try to divide number_1 on number_2\n")

    print("Your answer is: ", number_1 / number_2)
except ValueError:
    print("Convert unsuccessful")
except ZeroDivisionError:
    print("Dividing by zero")
except BaseException:
    print("Common exception")

print("\nEnd of the program")
