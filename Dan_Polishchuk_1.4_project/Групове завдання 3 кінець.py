def func():
    print("1 > e > 0")
    print("|an−(an−1)| < ε")
    e = float(input("Введіть значення е від 0 до 1:"))
    a = 0.75
    i = 3
    while True:
        a *= (1-(1/i**2))
        i += 1
        if abs(a - (a/((1-(1/(i-1)**2))))) < e:
            print("Перше число для якого виконується нерівність = ", a)
            break
func()