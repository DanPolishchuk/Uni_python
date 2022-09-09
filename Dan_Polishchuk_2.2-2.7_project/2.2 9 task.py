import re

text = "В        цьому " \
       "\nреченні розриви рядків... Але це " \
       "\nне так важливо! Зовсім? Так, зовсім! І це не повинно   заважати."

match0 = re.sub(r"\s+", " ", text)

patterns = [r".+\.\.\.", r"А.+о\!", r"З.+\?", r"Т.+\!", r"І.+"]

for i in range(len(patterns)):
       match1 = re.findall(patterns[i], str(match0))
       print(*match1)
