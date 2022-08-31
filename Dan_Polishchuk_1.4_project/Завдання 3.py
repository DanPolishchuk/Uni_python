while True:
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    number3 = int(input("Введіть третє число: "))
    if number1 > number2 > number3 or number1 > number3 > number2:
        print("Число, що більше = ", number1)
    elif number2 > number1 > number3 or number2 > number3 > number1:
        print("Число, що більше = ", number2)
    elif number3 > number2 > number1 or number3 > number1 > number2:
        print("Число, що більше = ", number3)
    else:
        print("Числа однакові")