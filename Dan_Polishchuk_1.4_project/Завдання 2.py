while True:
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    if number1 > number2:
        print("Число, що більше = ", number1)
    elif number1 == number2:
        print("Числа однакові")
    else:
        print("Число, що більше = ", number2)
