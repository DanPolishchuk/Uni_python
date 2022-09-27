import os
import pickle
import csv

def func(path, type1, type2):
    if type1 == ".txt" and type2 == ".dat":
        with open(path+"/task.txt", "r") as file:
            content = file.read()
        with open(path+"/task.dat", "wb") as file1:
            pickle.dump(content, file1)
        os.startfile(path+"/task.dat")
    if type1 == ".txt" and type2 == ".csv":
        with open(path+"/task.txt", "r") as file:
            content = file.read()
        with open(path+"/task.csv", "w", newline="") as file1:
            writer = csv.writer(file1)
            writer.writerow(content)
        os.startfile(path+"/task.csv")
    if type1 == ".csv" and type2 == ".dat":
        with open(path+"/task.csv", "r", newline="") as file:
            content = csv.reader(file)
            for row in content:
                with open(path+"/task.dat", "wb") as file1:
                    pickle.dump(row, file1)
        os.startfile(path+"/task.dat")
    if type1 == ".csv" and type2 == ".txt":
        with open(path+"/task.csv", "r", newline="") as file:
            content = csv.reader(file)
            for row in content:
                with open(path+"/task.txt", "a") as file1:
                    for i in range(len(row)):
                        file1.write(row[i])
        os.startfile(path+"/task.txt")
    if type1 == ".dat" and type2 == ".txt":
        with open(path+"/task.dat", "rb") as file:
            content = pickle.load(file)
            for i in content:
                with open(path+"/task.txt", "a") as file1:
                    file1.write(i)
        os.startfile(path+"/task.txt")
func("C:/lab4", ".txt", ".csv")