from pymongo import MongoClient
from pprint import pprint

client = MongoClient("localhost", 27017)

db = client["pets"]

collection1 = db["Dogs_Cats"]
collection2 = db["Others"]

pet_names = ["Jakob", "Sinan", "Mirco", "Samuel", "Donatello", "Rafael"]
breeds = ["dog:labrador", "cat:british_shorthair", "dog:dobermann", "rabbit", "snake", "parrot"]
age = [1, 3, 5, 3, 2, 10]

def insert(collection, start, finish):
    for i in range(start, finish):
        document = {"name": f"{pet_names[i]}",
             "breed": f"{breeds[i]}",
             "age": f"{age[i]}"}
        collection.insert_one(document).inserted_id

def show_documents(collection):
    documents = collection.find()
    for document in documents:
        pprint(document)

if __name__ == "__main__":
    show_documents(collection1)
    show_documents(collection2)
