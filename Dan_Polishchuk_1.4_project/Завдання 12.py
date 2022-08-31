print("Дано:y=x³-x²+x-1 ")
beg = int(input("Введіть початок діапазону: "))
stop = int(input("Введіть кінець діапазону: "))
step = int(input("Введіть крок : "))
for x in range(beg, stop+1, step):
    y = x**3+x**2+x-1
    print("якщо x =", x, " то у = ", y)