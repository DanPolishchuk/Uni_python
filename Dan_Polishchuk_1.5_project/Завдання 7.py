matrix = []
for i in range(3):
    matrix.append([])
for i in range(3):
    for j in range(3):
        matrix[i].append([int(str(i)+str(j))])
for i in range(0, len(matrix)):
    print(matrix[i])
