import os

user_dir = str(input("Type your path to create a directory: "))
os.mkdir(user_dir)
os.startfile(user_dir)

if os.path.exists(user_dir):
    print("Directory", user_dir, "was created")
else:
    print("Directory", user_dir, "wasn`t created")

user_file = str(input("If you want create a file in your dir, type it`s name: "))
with open(user_dir+"/"+user_file, "a") as file:
    file.write("File was created")
os.startfile(user_dir+"/"+user_file)

user_rename = str(input("Do you want to rename this file: "))
if user_rename == "yes":
    user_new_name = input("Type new file name: ")
    os.rename(user_dir+"/"+user_file, user_dir+"/"+user_new_name)
    print("Name was changed")
os.startfile(user_dir+"/"+user_new_name)

user_remove_file = str(input("Do you want to remove your file: "))
if user_remove_file == "yes":
    os.remove(user_dir+"/"+user_new_name)
    print("File was removed")

user_remove_dir = input("Do you want to remove this directory: ")
if user_remove_dir == "yes":
    os.rmdir(user_dir)
    print("Directory", user_dir, "was removed")


path = "c:\\user\tasks\new"
print(path)                                        #example of usage raw strings
path1 = r"c:\user\tasks\new"
print(path1)