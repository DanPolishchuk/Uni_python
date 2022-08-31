from random import *
n = int(input("Введіть кількість елементів списку: "))
a = []
for i in range(n):
    a.append(randint(-100, 100))
print(a, "- список")
for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] < a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a, "- список відсортований за спаданням")