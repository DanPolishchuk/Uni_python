import re;

user_text = input("Type your text : ")

match = re.findall(r"\b\D", user_text)

i = 0
while i < (len(match)-1):
    match[0] += match[i+1]
    i += 1

print(match[0].upper())