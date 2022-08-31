import random
n = int(input("Введіть кількість рядків матриці : "))
m = int(input("Введіть кількість стовпців матриці : "))
matrix = []
for i in range(n):
    matrix.append([])
for i in range(n):
    for j in range(m):
        matrix[i].append(random.randint(-100, 100))
for i in range(0, len(matrix)):
    print(matrix[i])
s = set()
for i in range(len(matrix)):
    s.add(sum(matrix[i]))
print(s, "- сет з сум елементів рядків матриці")