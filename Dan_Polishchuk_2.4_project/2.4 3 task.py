import os
while True:
    user_date = input("Type your date: ")
    user_event = input("Type your event: ")
    with open(r"c:\lab4\Calendar.txt", "a") as file:
        file.write("\n" + user_date + "\t" + user_event)
    os.startfile(r"c:\lab4\Calendar.txt")
    user_choice = input("Would you like to add another one event: ")
    if user_choice == "no":
        break
os.remove(r"c:\lab4\Calendar.txt")