def func():
    print("Дано:\n x³-40x-1>0")
    for x in range(1, 1000):
        if x**3-40*x-1>0 and (x-1)**3-40*(x-1)-1<0 :
            print("Найменше ціле значення х =", x)
func()