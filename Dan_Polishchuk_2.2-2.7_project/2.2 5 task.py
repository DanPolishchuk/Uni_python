import re; user_text = input("Type your text : "); match = re.findall(r"\b\w", user_text); abbreviation = "".join(match); print(abbreviation.upper())