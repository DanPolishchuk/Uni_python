import random
print("Завдання 5")
dict1 = dict()
list1 = ["Kate", "Dan", "Alex", "Max", "Karl", "Frank", "Natali", "Jason", "Mikey", "Bob", "Steph", "Tony", "Steve"]
while True:
    if len(dict1) != 10:
        dict1[random.randint(0, 1000)] = random.choice(list1)
    else:
        break
print(dict1)
print("Завдання 6")
for i in dict1:
    if i % 2 == 0:
        dict1[i] = "Парне значення"
print(dict1)