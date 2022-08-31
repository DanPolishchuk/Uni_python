from math import *
while True:
    side1 = int(input("Введіть першу сторону трикутника: "))
    side2 = int(input("Введіть другу сторону трикутника: "))
    side3 = int(input("Введіть третю сторону трикутника: "))
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        print("0 - трикутника не існує")
    else:
        p = (side1+side2+side3)/2
        s = sqrt(p*(p-side1)*(p-side2)*(p-side3))
        print(s)