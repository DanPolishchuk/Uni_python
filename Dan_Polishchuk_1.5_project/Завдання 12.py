import random
a = list()
for i in range(11):
    a.append(random.randint(0, 20))
print(a, "- Список")
for i in range(1, len(a)):
    a[0] += a[i]
print(a[0], "- Сума всіх елементів списку")
