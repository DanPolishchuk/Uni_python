from random import randint
print("Завдання 1")
list1 = list()
print("Завдання 2")
for i in range(1, 11):
    list1.append(randint(0, 100))
print(list1)
print("Завдання 3")
i = 2
n = len(list1)
while i < n:
    list1.pop(i)
    n -= 1
    i += 2
print(list1)
print("Завдання 4")
print("Сума елементів списку = ", sum(list1))