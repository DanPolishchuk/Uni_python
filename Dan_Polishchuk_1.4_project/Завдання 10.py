def func():
        n = int(input("Введіть число: "))
        factorial = 1
        for i in range(1, n+1):
            factorial = factorial*i
        print("Факторіал числа = "+str(factorial))
func()