from random import *
n = int(input("Введіть кількість елементів списку: "))
a = tuple()
for i in range(n):
    a += (randint(-100, 100),)
print(a, "- кортеж")
sum = 0
for i in range(0, len(a), 2):
    sum += a[i]
print(sum, "- сума елементів кортежу с парними індексами")
