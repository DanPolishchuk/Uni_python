def func():
    f1 = f2 = 1
    n = int(input("Введіть номер елементу числа Фібоначчі :"))
    for i in range(2, n):
        fn = f1+f2
        f1 = f2
        f2 = fn
    print("Число = " + str(f2))
func()