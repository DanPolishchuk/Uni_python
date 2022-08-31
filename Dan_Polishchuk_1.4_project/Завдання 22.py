def func():
    C = int(input("Введіть значення С :"))
    a = 1
    i = 1
    while True :
        a += (1 + 1/i)
        i += 1
        if a > C:
            print("Номер елементу що більший за С = ", i)
            break
func()