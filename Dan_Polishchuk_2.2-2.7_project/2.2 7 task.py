import re

text = "Дуже поширена помилка помилка - це лише повторення повторення слова слова. Смішно, чи чи не так? Це - книга книгарні."

match = re.findall(r"[\w?.-]+", text)

for i in range(len(match)-5):
    match1 = re.findall(r"\w+", match[i])
    match2 = re.findall(r"\w+", match[i+1])
    if match1 == match2:
        match.pop(i)

print(text)

print(*match)
