def func():
    print("Введіть координати площини")
    x1 = int(input("x1 : "))
    x2 = int(input("x2 : "))
    y1 = int(input("y1 : "))
    y2 = int(input("y2 : "))
    print("Введіть координати точки")
    x = int(input("x : "))
    y = int(input("y : "))
    if (x2 > x > x1 or x1 > x > x2) and (y2 > y > y1 or y1 > y > y2):
        print("Точка належить площині")
    else:
        print("Точка не належить площині")
func()