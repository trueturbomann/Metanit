try:
    number_1 = int(input("Enter number_1 "))
    number_2 = int(input("Enter number_2 "))
    print(number_1 / number_2)

except ValueError as e:
    print("Information about exception:", e)

print("\nEnd of the program")