from math import *
while True:
    k = int(input("Введіть k: "))
    x = int(input("Введіть х: "))
    if k == 1:
        y = x
        print("x=", x, "y=", y)
    elif k == 2:
        y = sqrt(x)
        print("x=", x, "y=", y)
    elif k == 3:
        y = x**2
        print("x=", x, "y=", y)
    else:
        y = 0
        print("x=", x, "y=", y)