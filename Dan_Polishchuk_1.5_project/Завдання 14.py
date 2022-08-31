import random
n = int(input("Введіть кількість елементів :"))
a = list()
for i in range(n):
    a.append(random.randint(1, 100))
print(a, "- список")
s = 0
for i in range(0, len(a)):
    if a[i] > (sum(a)/n):
        s += 1
print("Середнє значення списку = ", (sum(a)/n))
print("Кількість елементів, які більші за середнє значення списку = ", s)
