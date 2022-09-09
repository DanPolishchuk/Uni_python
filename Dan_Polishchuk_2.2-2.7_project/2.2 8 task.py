import re

user_text = input("Type your text : ")

match0 = re.findall(r"\w+", user_text)

match1 = re.findall(r"\d+", user_text)

for i in range(len(match0)):
    for j in range(len(match1)):
        if match0[i] == match1[j]:
            match0[i] = format(int(match0[i]), ",")

print(*match0)



