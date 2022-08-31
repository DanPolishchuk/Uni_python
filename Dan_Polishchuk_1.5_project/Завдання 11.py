import random
print("1.")
a = list()
b = list()
c = list()
d = list()
for i in range(5):
    a.append(random.randint(0, 15))
    b.append(random.randint(0, 15))
    c.append(random.randint(0, 15))
    d.append(random.randint(0, 15))
print(a, "- list 1")
print(b, "- list 2")
print(c, "- list 3")
print(d, "- list 4")
print(a + b, "- list 1 + list 2")
c.extend(d)
print(c, "- list 3 + list 4")
print("2.")
print(len(a), "- довжина списку 1")
print(len(c + d), "- довжина списку 3 + довжина списку 4")
print("3.")
if random.randint(0, 15) in a:
    print("Елемент є в списку 1")
else:
    print("Елементу немає в списку 1")
f = a + b + c + d
if random.randint(0,15) in f:
    print("Елемент є в усіх списках")
else:
    print("Елементу немає в жодному списку")