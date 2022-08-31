print("Алгоритм Евкліда")
def func():
    num1 = int(input("Введіть перше число : "))
    num2 = int(input("Введіть друге число : "))
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    print("НСД = ", num1)
func()