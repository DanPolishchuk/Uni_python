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
t = tuple()
for i in range(m):
    max = 0
    for j in range(n):
        if matrix[j][i] > max:
            max = matrix[j][i]
    t += (max,)
print(t, "- кортеж з максимальних значень стовпців матриці")
