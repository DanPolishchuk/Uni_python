import re

text = 'Регулярні вирази є схожим, але набагато сильнішим інструментом. для пошуку рядків, їх перевірки на ' \
         'відповідність якомусь шаблону та іншій подібній роботі. Англомовна назва цього інструменту – Regular ' \
         'Expressions або просто RegExp. Строго кажучи, регулярні вирази – спеціальна мова для опису шаблонів ' \
         'рядків.\n\nАААА аааа АаАаАаАа 123 123 12345 11223344 А1Б2В3 АА11 ББ22ВВ 33ГГ44\n\nТест! Ще! Даєш! ' \
         'ЇЇ\n\nQwertyЙцукен\n\n+-,/, *** (**), a(b+[c+d])*e/f+g-h\n\n!!"""####\n\n\n' \
         "$%%%%%&&&'''((((())***++++,,,,,-----..// :::;;;;<<<<<===>>>????? @@@@@[[[[\]]]]]]^^^__``{{{{|||||}}}}}~~~~~" \
         '\n\n<a href="#10">10: CamelCase -> under_score</a>;\n<a href="#11">11: Видалення повторів</a>;\n<a href="#12">12: ' \
         'Близькі слова</a>;\n<a href="#13">13: Форматування великих чисел</a>;\n<a href="#14">14: Розділити текст на ' \
         'пропозиції</a>;\n<a href="#15">15: Форматування номера телефону</a>;\n<a href="#16">16: Пошук e-mailів — 2</a>;'

match = re.findall(r'\b[АаЕеЄєИиУуЇїОоІіЮю]\w+', text)

print(match)

if match:
    print("There are at least one match")
else:
    print("Unfortunately....:(")