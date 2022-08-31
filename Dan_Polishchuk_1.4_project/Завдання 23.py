import math
def func():
    print("|an−(an−1)|>ε")
    x = int(input("Введіть значення x :"))
    e = float(input("Введіть значення e :"))
    a = 1
    k = 1
    while True :
        a += (x ** k) / math.factorial(k)
        k += 1
        if abs(a - (a - (x ** (k-1)) / math.factorial(k-1))) > e:
            print("Перше число для якого виконувається нерівнять = ", a)
            break
func()


