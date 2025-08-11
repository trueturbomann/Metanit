try:
    age = int(input("Enter age: "))
    if age > 110 or age < 1 :
        raise Exception("Wrong age")
    print("Your age is:", age)
except ValueError:
    print("Wrong input value")

except Exception as e:
    print(e)
print("\nEnd of the program")