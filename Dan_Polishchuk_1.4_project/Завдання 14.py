print("Дано:\n x³-40x-1>0")
min = 1
for x in range(min, 1000):
    if x**3-40*x-1 > 0 and (x-1)**3-40*(x-1)-1 < 0:
        print("Найменше ціле значення х =", x)