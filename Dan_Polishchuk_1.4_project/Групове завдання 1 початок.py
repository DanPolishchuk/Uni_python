def func():
    n = int(input("Введіть значення n :"))
    a = 0.5
    for i in range(2, n+1):
        a += 1/(1+i**2)
    print("an = ", a)
func()

