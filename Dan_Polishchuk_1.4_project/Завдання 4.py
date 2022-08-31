while True:
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    number3 = int(input("Введіть третє число: "))
    if number1 > number2 > number3 or number1 > number3 > number2:
        if number1 > 0:
            print(number1**3)
        else:
            print("Число менше нуля")
    elif number2 > number1 > number3 or number2 > number3 > number1:
        if number2 > 0:
            print(number2 ** 3)
        else:
            print("Число менше нуля")
    elif number3 > number2 > number1 or number3 > number1 > number2:
        if number3 > 0:
            print(number3 ** 3)
        else:
            print("Число менше нуля")
