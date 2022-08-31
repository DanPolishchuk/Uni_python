import random
n = int(input("Введіть кількість елементів 1 списку: "))
m = int(input("Введіть кількість елементів 2 списку: "))
a = list()
b = list()
for i in range(0, n):
    a.append(random.randint(-100, 100))
for i in range(0, m):
    b.append(random.randint(-100, 100))
c = a + b
def sort(list):
    for i in range(len(list)-1):
        for j in range(len(list)-1-i):
            if list[j] >= list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
sort(a)
sort(b)
sort(c)
print(a, "- список 1")
print(b, "- список 2")
print(c, "- список 3")