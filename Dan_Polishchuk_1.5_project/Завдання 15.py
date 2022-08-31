import random
n = int(input("Введіть кількість елементів :"))
a = list()
for i in range(n):
    a.append(random.randint(1, n*2))
print(a, "- список")
if len(a) != len(set(a)):
    print("True")
else:
    print("False")
