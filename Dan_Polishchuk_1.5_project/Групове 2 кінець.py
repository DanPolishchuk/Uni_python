from random import *
n = int(input("Введіть кількість елементів списку: "))
a = []
for i in range(n):
    a.append(randint(-100, 100))
print(a)
k = 0
for i in a:
    if i < 0:
        k = 1
for i in range(len(a)):
    if k == 1 and i % 2 == 0:
        k = 2
if k == 2:
    print("True")
else:
    print("False")

