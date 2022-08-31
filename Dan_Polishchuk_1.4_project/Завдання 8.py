print("Задано n (n≥1) цілих чисел (a1,a2,…,an )")
n = int(input("Введіть n :"))
max = 0
for i in range(n):
    a1 = int(input("Введіть число :"))
    if a1 > max:
        max = a1
print("Максимальне значення = " + str(max))



