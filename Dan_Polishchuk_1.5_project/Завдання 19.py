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
s = 0
for i in range(len(matrix)):
    if matrix[i][i] < 0:
        s = 1
if s == 1:
    print("Від'ємні елементи в діагоналі матриці існують")
else:
    print("Від'ємних елементів немає в діагоналі матриці")