import re

user_text = input("Type your text : ")

mylist = []

match = re.findall(r"[A-Za-zА-Яа-я]+", user_text)

for i in range(len(match)):
    match[i] = match[i].upper()
    i += 1

mylist.append(match[0][0])

for i in range(1, len(match)):
    mylist[0] += match[i][0]
    i += 1

print(mylist)