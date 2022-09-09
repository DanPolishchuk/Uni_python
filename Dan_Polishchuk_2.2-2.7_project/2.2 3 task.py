import re

user_text = input("Type your text : ")

match = re.findall(r'^[\w.-]+@[A-Z-a-zА-Яа-я-\d]+\.[A-Z-a-zА-Яа-я-\d]+', user_text)
if match:
    print("Your e-mail is valid :)")
else:
    print("Your e-mail isn`t valid :(")