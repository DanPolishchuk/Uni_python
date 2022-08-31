def func():
    side1 = int(input("Введіть першу сторону трикутника :" ))
    side2 = int(input("Введіть другу сторону трикутника :" ))
    side3 = int(input("Введіть третю сторону трикутника :" ))
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        print("0 - трикутника не існує")
    else:
        print("1 - трикутник існує")
func()
    