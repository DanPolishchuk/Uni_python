import re

user_text = input("Type your text : ")
mylist = []
password = "qwerty123"

match = re.findall(r'[A-Za-zА-Яа-я-\d]+', user_text)

for i in range(len(match)):
    match[i] = match[i].lower()
    i += 1

mylist.append(match[0])

for i in range(1, len(match)):
    mylist[0] += match[i]
    i += 1

if mylist[0] == password:
    print("Your password is accepted :)")
else:
    print("Your password is wrong :(")