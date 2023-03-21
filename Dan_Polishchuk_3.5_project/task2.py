import sqlite3

def age():
        
    age = int(input("Type your age: "))
    if age >= 18:
        print("Congrats you are allowed to buy alcohol!!!")
    else:
        print("You are such a little pussy, do your homework(")
 
################################################################################################

def password():
        
    password = "AsusLenovo"
    check = input("To log in enter your password ********vo :")
    if check == password:
        print("You`ve successfully logged in")
    else:
        raise Exception ("Your password is not correct")

#################################################################################################

def ask_user_for_path():
    path = input("Enter the file path: ")
    return path

################################################################################################

def read_file(path):
    with open(path, "r") as f:
        data = f.read()
        print(data)

#################################################################################################
def connect_to_database():
    conn = sqlite3.connect("C:\\Uni_tasks\\Dan_Polishchuk_3.5_project\\mydatabase.db")
    cursor = conn.cursor()
    table = input("Provide a table name: ")
    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)


################################################################################################################

if __name__ == "__main__":

    try:
        age()

    except ValueError:
        print("Please enter only numbers")
    
    try:
        password()
    
    except Exception as e:
        print(e)
    
    try:
        read_file("C:\\Uni_tasks\\Dan_Polishchuk_3.5_project\\data.txt")
    
    except Exception:
        print("File not found!")
        new_path = ask_user_for_path()
        read_file(new_path)

    try:
        connect_to_database()
    
    except sqlite3.OperationalError:
        print("This table does not exist!")

#######################################################################################################################
    class MyException(Exception):
        pass

    try:
        raise MyException("This is my custom exception!")
    
    except MyException as e:
        print(e)
