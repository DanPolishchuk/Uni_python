import math
print("Дано n! >= C")
C = int(input("Введіть С :"))
for n in range(0, 10000):
    if math.factorial(n) >= C and math.factorial(n-1) <= C :
        print("Найменше n = ", n)
