import re

text = "Дуже поширена помилка помилка - це лише повторення повторення слова слова. Смішно, чи чи не так? Це - книга книгарні."

match = re.findall(r"[\w?.-]+", text)

mylist = []

for i in range(len(match) - 1):
    if match[i] != match[i+1]:
        mylist.append(match[i])

print(text)

print(*mylist)