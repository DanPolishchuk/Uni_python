from datetime import datetime

now = datetime.now()
print("Date:", "\nUkraine: ", now.strftime("%d.%m.%Y"))
print("Lithuania: ", now.strftime("%Y-%m-%d"))
print("USA: ", now.strftime("%m/%d/%Y"))