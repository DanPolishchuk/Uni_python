from random import *
listt = []
n = int(input("Введіть кількість рядків: "))
m = int(input("Введіть кількість стовпців: "))
for i in range(n):
    listt.append([])
    for j in range(m):
        listt[i].append(randint(0, 100))
for i in range(len(listt)):
    print(listt[i])
b = []
for i in range(n):
    max = listt[0][j]
    for j in range(m):
        if listt[i][j] > max:
            max = listt[i][j]
    b += (max,)
print(b, "- список з максимальних значень рядків матриці")