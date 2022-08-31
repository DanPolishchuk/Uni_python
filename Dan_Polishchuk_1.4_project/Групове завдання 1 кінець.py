def minim():
    global minim
    n = int(input("Введіть кількість членів послідовності :"))
    for i in range(n):
        a1 = int(input("Введіть число :"))
        minim = a1
        if a1 < minim:
            minim = a1
    print("Мінімальне значення = ", minim)
minim()