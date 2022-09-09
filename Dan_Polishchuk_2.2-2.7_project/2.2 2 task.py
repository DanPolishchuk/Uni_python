import re
user_text = str(input("Type your car numbers as it`s written below\n XX 1234 XX : "))

match = re.findall(r"\w{2}\s\d{4}\s\w{2}", user_text)

if match:
    if match[0][0] == "К" and match[0][1] == "А":
        print("Your numbers is valid, and your auto was registered in Kyiv")
    elif match[0][0] == "К" and match[0][1] == "Н":
        print("Your numbers is valid, and your auto was registered in Donetsk region")
    elif match[0][0] == "К" and match[0][1] == "Х":
        print("Your numbers is valid, and your auto was registered in Kharkiv region")
    else:
        print("Your numbers is valid, but your auto was registered not in Kyiv city, Kharkiv region or Donetsk region")
else:
    print("Your numbers are not valid")
