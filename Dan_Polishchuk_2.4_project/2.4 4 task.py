from datetime import datetime

user_text = input("Type when you have been born(year-month-day): ")
now = datetime.now()
mylist = [user_text+" 0:0:0.0"]
DB = datetime.strptime(mylist[0], "%Y-%m-%d %H:%M:%S.%f")
print("Your age is: ", now - DB)