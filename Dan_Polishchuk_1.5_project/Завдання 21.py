import random
n = int(input("Введіть кількість елементів :"))
a = list()
for i in range(n):
    a.append(random.randint(1, 100))
print(a, "- список")
for i in range(1, len(a)):
    a[0] += a[i]
print("Середнє значення списку = ", a[0]/n)