from random import *
n = int(input("Введіть кількість елементів списку: "))
c = int(input("Введіть значення С: "))
a = []
for i in range(n):
    a.append(randint(-100, 100))
a.sort()
print(a, "- список")
for i in range(1, len(a)):
    if i % 7 == 0:
        a.insert(i+1, c)
print(a)

