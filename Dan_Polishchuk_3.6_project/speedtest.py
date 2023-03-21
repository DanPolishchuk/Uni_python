from pymongo import MongoClient
from sqlite3 import connect
from time import time


def mongodb():
    start_time = time()
    client = MongoClient("localhost", 27017)
    db = client["Test"]
    collection = db["Test"]
    i = 0
    while i < 10000:
        document = {"test": "test"}
        collection.insert_one(document)
        i += 1
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"MongoDB впоралась за {elapsed_time} секунд")


def sqlite():
    start_time = time()
    conn = connect("C:\\Uni_tasks\\Dan_Polishchuk_3.6_project\\Test.db")
    cur = conn.cursor()
    i = 0
    cur.execute("""CREATE TABLE Test(test)""")
    while i < 10000:
        cur.execute(f"""INSERT INTO Test(test) VALUES("test")""")                   
        i += 1
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Sqlite впоралась за {elapsed_time} секунд")


mongodb()
sqlite()