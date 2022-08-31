import math
print("Задано n (n≥1) дійсних чисел (i = 1, …, n)")
n = int(input("Введіть n :"))
avg = 0
for i in range(n):
    a1 = int(input("Введіть число :"))
    avg = avg + a1
    avrg = avg / n
print("Середнє значення = " + str(avrg))

