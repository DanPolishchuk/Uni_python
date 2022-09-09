import re

user_text = [["Ще не померла! / Закінчується осінь, / Я йду за обрій."],
             ["Ночую просто неба. / Виє пес. / Теж допекла, мабýть, осіння мряка!"],
             ["Вода замерзла, / Розколовши глечик. / І тріск раптовий розбудив мене."]]

text = [["Ще не померла! /"], ["Закінчується осінь, /"], ["Я йду за обрій."],
       ["Ночую просто неба. /"], ["Виє пес. /"], ["Теж допекла, мабýть, осіння мряка!"],
       ["Вода замерзла, /"], ["Розколовши глечик. /"], ["І тріск раптовий розбудив мене."]]

pattern = (r'[АаЯяУуЕеЄєОоІіИиЮюЇї]')

for i in range(1):
    for j in range(len(text[i])):
        mylist1 = []
        match = re.findall(pattern, text[i][j])
        mylist1.append(match)
        for k in range(1, 2):                                      # створення першого списка с першим Хайку
            for n in range(len(text[k])):
                match = re.findall(pattern, text[k][n])
                mylist1.append(match)
                for m in range(2, 3):
                    for x in range(len(text[m])):
                        match = re.findall(pattern, text[m][x])
                        mylist1.append(match)
for i in range(3, 4):
    for j in range(len(text[i])):
        mylist2 = []
        match = re.findall(pattern, text[i][j])
        mylist2.append(match)
        for k in range(4, 5):                                       # створення другого списка с другим Хайку
            for n in range(len(text[k])):
                match = re.findall(pattern, text[k][n])
                mylist2.append(match)
                for m in range(5, 6):
                    for x in range(len(text[m])):
                        match = re.findall(pattern, text[m][x])
                        mylist2.append(match)
for i in range(6, 7):
    for j in range(len(text[i])):
        mylist3 = []
        match = re.findall(pattern, text[i][j])
        mylist3.append(match)
        for k in range(7, 8):                                    # створення третього списка с третім Хайку
            for n in range(len(text[k])):
                match = re.findall(pattern, text[k][n])
                mylist3.append(match)
                for m in range(8, 9):
                    for x in range(len(text[m])):
                        match = re.findall(pattern, text[m][x])
                        mylist3.append(match)

if len(mylist1[0]) != 5:
    print(user_text[0], "У першому рядку ", len(mylist1[0]), "складів а потрібно 5! НЕ ХАЙКУ :(" )
elif len(mylist1[1]) != 7:
    print(user_text[0], "У другому рядку ", len(mylist1[1]), "складів а потрібно 7! НЕ ХАЙКУ :(" )         # перевірка першого Хайку
elif len(mylist1[2]) != 5:
    print(user_text[0], "У третьому рядку ", len(mylist1[2]), "складів а потрібно 5! НЕ ХАЙКУ :(" )
else:
    print(user_text[0], "ХАЙКУ! :)")

if len(mylist2[0]) != 5:
    print(user_text[1], "У першому рядку ", len(mylist2[0]), "складів а потрібно 5! НЕ ХАЙКУ :(" )
elif len(mylist2[1]) != 7:
    print(user_text[1], "У другому рядку ", len(mylist2[1]), "складів а потрібно 7! НЕ ХАЙКУ :(" )         # перевірка другого Хайку
elif len(mylist2[2]) != 5:
    print(user_text[1], "У третьому рядку ", len(mylist2[2]), "складів а потрібно 5! НЕ ХАЙКУ :(" )
else:
    print(user_text[1], "ХАЙКУ! :)")

if len(mylist3[0]) != 5:
    print(user_text[2], "У першому рядку ", len(mylist3[0]), "складів а потрібно 5! НЕ ХАЙКУ :(" )
elif len(mylist3[1]) != 7:
    print(user_text[2], "У другому рядку ", len(mylist3[1]), "складів а потрібно 7! НЕ ХАЙКУ :(" )         # перевірка третього Хайку
elif len(mylist3[2]) != 5:
    print(user_text[2], "У третьому рядку ", len(mylist3[2]), "складів а потрібно 5! НЕ ХАЙКУ :(" )
else:
    print(user_text[2], "ХАЙКУ! :)")