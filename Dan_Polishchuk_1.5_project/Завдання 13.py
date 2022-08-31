import random
print("C <= ai <= D")
n = int(input("Введіть кількість елементів в списку :"))
c = int(input("Введіть значення С:"))
d = int(input("Ввведіть значення D:"))
ai = list()
for i in range(0, n):
    ai.append(random.randint(1, 1000))
print(ai, "- список")
a = 0
for i in range(0, len(ai)):
    if c <= ai[i] <= d:
        a += 1
print("Кількість елементів задовольняючих нерівність = ", a)

