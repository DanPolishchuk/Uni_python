n = int(input("Введіть кількість членів послідовності :"))
max = 0
for i in range(n):
    a1 = int(input("Введіть число :"))
    if a1 > max:
        max = a1
print("Максимальне значення = " + str(max))