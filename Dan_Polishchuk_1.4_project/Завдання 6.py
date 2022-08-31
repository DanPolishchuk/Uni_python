while True:
    number1 = int(input("Введіть перше число: "))
    number2 = int(input("Введіть друге число: "))
    number3 = int(input("Введіть третє число: "))
    print(number1 ** 3) if (number1 > 0 and (number1 >= number2 >= number3 or number1 >= number3 >= number2)) else print(number2 ** 3) if (number2 > 0 and (number2 >= number1 >= number3 or number2 >= number3 >= number1)) else print(number3 ** 3) if (number3 > 0 and (number3 >= number2 >= number1 or number3 >= number1 >= number2)) else print("Число менше нуля")