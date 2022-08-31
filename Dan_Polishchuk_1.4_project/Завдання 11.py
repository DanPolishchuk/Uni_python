import math
def func():
    n = int(input("Введіть число: "))
    sumf = 1
    for i in range(2, n+1):
        sumf = sumf + math.factorial(i)
    print("Результат = "+str(sumf))
func()
