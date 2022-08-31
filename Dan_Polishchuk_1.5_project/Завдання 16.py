import random
n = int(input("Введіть кількість елементів :"))
a = list()
for i in range(n):
    a.append(random.randint(1, 100))
print(a, "- список")
s = 0
for i in range(0, (len(a)-1)):
    if a[i] < a[i+1]:
        print("True")
        exit()
print("False")
