# from task1 import DB
from sqlite3 import connect

dataset_path = "C:\\Uni_tasks\\Dan_Polishchuk_3.2_project\\owid_covid_data.csv"
sqlite_path = "C:\\Uni_tasks\\Dan_Polishchuk_3.2_project\\owid_covid_data.db"

# Cowid = DB(dataset_path, sqlite_path)
# Cowid.type_definition()

#######################################################################################################################

table_name = "owid_covid_data"
conn = connect(sqlite_path)
cur = conn.cursor()


def query(request):
    cur.execute(request)
    rows = cur.fetchall()
    return rows


task1 = query(f"""SELECT total_cases FROM {table_name} 
              WHERE date="2020-08-30" AND location="Philippines" """)

########################################################################################################################

task2_ukraine_total_cases = query(f"""SELECT total_cases FROM {table_name}
                                  WHERE location="Ukraine" """)
total_cases = []
for i in range(len(task2_ukraine_total_cases)):
    total_cases.append(task2_ukraine_total_cases[i][0])

increase = 0.0
difference = 0.0
i = 0
while i < (len(total_cases) - 7):
    if total_cases[i + 7] - total_cases[i] > increase:
        difference = total_cases[i + 7] - total_cases[i]
        increase = total_cases[i + 7]
    i += 7
task2_date_of_biggest_increase = query(f"""SELECT date FROM {table_name}
                                       WHERE location="Ukraine" AND total_cases={increase} """)

########################################################################################################################

task3_continents_total_cases = query(f"""SELECT sum(total_cases) FROM {table_name}
                              WHERE location IN 
                              ("North America", "South America", "Africa", "Europe", "Asia", "Oceania", "International")
                              AND date="2020-08-21" """)

task3_world_total_cases = query(f"""SELECT total_cases FROM {table_name}
                                WHERE location="World" AND date="2020-08-21" """)

########################################################################################################################

all_countries_data = []
countries = query(f"""SELECT DISTINCT location FROM {table_name}
                  WHERE location NOT in 
                  ("North America", "South America", "Africa", "Europe", "Asia", "Oceania", "International", "World")
                  """)
for i in range(len(countries)):
    all_countries_data.append(countries[i][0] + " - " + str(query(f"""SELECT max(total_cases) FROM {table_name} 
                                                                  WHERE location="{countries[i][0]}" """)[0][0]))
for i in all_countries_data:
    with open("C:\\Uni_tasks\\Dan_Polishchuk_3.2_project\\owid_covid_data.txt", "a") as file:
        file.write("\n" + i)

########################################################################################################################

print("1. Total cases Philippines 30.08.2020 -", int(task1[0][0]))
print("\n2. The largest increase in patients per week was recorded in Ukraine -", task2_date_of_biggest_increase[0][0],
      ", +", int(difference), "cases")
print("\n3. Total cases across all continents 21.08.2020 -", int(task3_continents_total_cases[0][0]))
print("Total cases in the world 21.08.2020 -", int(task3_world_total_cases[0][0]))
