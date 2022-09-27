import csv
with open("c:/lab4/owid-covid-data.csv", "r", newline="") as file:
    data = list(csv.reader(file))
    for row in data:
        if row[2] == "Philippines" and row[3] == "2020-08-30":
            print("Task 1:\nTotal Philippines cases 2020-08-30 - ", row[4])
            break

    mylist = []
    for row in data:
        if row[2] == "Ukraine":
            mylist.append(float(row[4]))
        increase = 0.0
        difference = 0.0
        i = 0
        while i < (len(mylist) - 7):
            if (mylist[i+7] - mylist[i]) > increase:
                difference = (mylist[i+7] - mylist[i])
                increase = mylist[i+7]
            i += 7
    for row in data:
        if row[2] == "Ukraine" and row[4] == str(increase):
            print("\nTask 2:\nThe largest increase in patients per week was recorded in Ukraine - ",
                  row[3], ", +"+str(int(difference)))

    all_countries = 0.0
    for row in data[1:]:
        if row[4] == "":
            row[4] = 0.0
        else:
            row[4] = float(row[4])
        parts = ["North America", "South America", "Africa", "Europe", "Asia", "Oceania", "International"]
        for i in parts:
            if row[2] == i and row[3] == "2020-08-21":
                all_countries += row[4]
        if row[2] == "World" and row[3] == "2020-08-21":
            print("\nTask 3:\nTotal World cases 21.08.2022 - ", row[4])
    print("Total cases of all countries counted together 21.08.2022 - ", all_countries)

    mylist1 = []
    mylist2 = []
    maximum = 0.0
    for row in data[1:]:
        if row[2] not in mylist1:
            mylist1.append(row[2])
        i = 0
    while i < len(mylist1):
        mylist3 = []
        for row in data[1:]:
            if row[4] == "":
                row[4] = 0.0
            else:
                row[4] = float(row[4])
            if row[2] == mylist1[i]:
                mylist3.append(row[4])
        mylist2.append(max(mylist3))
        i += 1
    for i in range(len(mylist1)):
        mylist1[i] += (" : " + str(int(mylist2[i])))
        with open("c:/lab4/cowid_stats.txt", "a") as file:
            file.write("\n" + mylist1[i])












