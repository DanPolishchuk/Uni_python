import random
n = int(input("Введіть кількість елементів : "))
a = list()
for i in range(0, int(n/2)):
    a.append(random.randrange(0, 500, 2))
    a.append(random.randrange(1, 500, 2))
a.sort()
print(a, "- список")
d = dict()
pair = list()
unpair = list()
for i in a:
    if i % 2 == 0:
        pair.append(i)
    else:
        unpair.append(i)
for i in range(len(pair)):
    d[pair[i]] = unpair[i]
print(d, "- словник")



