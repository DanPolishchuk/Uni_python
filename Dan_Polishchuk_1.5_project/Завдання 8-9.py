import random
print("Завдання 8")
a = set()
for i in range(6):
    a.add(random.randint(0, 1000))
print(a, "- сет")
print("Завдання 9")
for i in a:
    print(i)
print(type(a), a)
a.add(666)
print(a, "додали елемент 666")
a.remove(666)
print(a, "- видалили елемент 666 ")
print(list(a), "- перетворили на список")
print(tuple(a), "- перетворили на  кортеж")
print(sum(a), "- сума сету")