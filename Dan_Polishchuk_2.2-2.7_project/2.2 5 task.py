import re; user_text = input("Type your text : "); match = re.findall(r"\b\w", user_text)

for i in range(1, len(match)):
    match[0] += (match[i])

print(match[0].upper())