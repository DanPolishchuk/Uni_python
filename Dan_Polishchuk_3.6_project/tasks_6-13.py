from pymongo import MongoClient
from pprint import pprint
from random import randint, choice
from csv import DictReader
from json import dumps, loads


client = MongoClient("localhost", 27017)

db = client["pets"]

################################################### 6 task #####################################################

owners = db["Owners"]

names = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer", "Michael", "Linda", "William", "Elizabeth"]
pet_names = ["Luna", "Bella", "Teddy", "Milo", "Dairy", "Lola", "Bailey", "Buddy", "Coco", "Poppy"]
pet_species = ["dog", "cat", "rabbit", "parrot"]

def insert_documents():
    for i in range(15):
        document = {"Owner`s name": choice(names),
                    "Owner`s age": randint(10, 90),
                    "Pet`s name": choice(pet_names), 
                    "Pet`s species": choice(pet_species),
                    "Pet`s age": randint(0, 10)}
        owners.insert_one(document).inserted_id

###################################################### 7 task ###################################################

ids1_list = []

def show_documents():
    documents = owners.find()
    for document in documents:
        pprint(document)
        ids1_list.append(document["_id"])

###################################################### 8 task ####################################################

def find_with_id(id):
    
    print("\nFound with id:\n")
    pprint(owners.find_one({"_id": id}))
    ids1_list.clear()

##################################################### 9 task #####################################################

def same_pet():
    for i in pet_species:
        print(f"\nOwners of {i}s :\n")
        for document in owners.find({"Pet`s species": i}):
            pprint(document)

###################################################### 10 task ##################################################

letters = ["LBTMDCP"]

def same_letter_at_start():
    for i in letters[0]:
        print(f"\nPet`s names that start with {i} :\n")
        for document in owners.find({"Pet`s name": {"$regex": f"^{i}"}}):
            pprint(document)

##################################################### 11 task ##################################################

def young_scientist():
    print("\nYoung scientists:\n")
    for document in owners.find({"Owner`s age": {"$lt": 35}, "Pet`s species": {"$in": ["cat", "dog"]}}):
        pprint(document)


################################################### 12-13 task ###################################################

ids2_list = []

def creating_collaction_from_csv():
    with open("C:\\Uni_tasks\\Dan_Polishchuk_3.6_project\\Housing.csv", "r") as f:
        reader = DictReader(f)
        data = [dict(row) for row in reader]

    json_data = dumps(data)

    housing = db["Housing"]
    
    housing.insert_many(loads(json_data))

    documents = housing.find()
    for document in documents:
        ids2_list.append(document["_id"])

    for i in ids2_list:
        has_pet = randint(1, 10)
        housing.update_one({"_id": i},
            {"$set":{"Owner`s name": choice(names),
            "Owner`s age": randint(10, 90),
            "Pet`s name": None if has_pet == 1 else choice(pet_names), 
            "Pet`s species": None if has_pet == 1 else choice(pet_species),
            "Pet`s age": None if has_pet == 1 else randint(0, 10)}}
        )

    ids2_list.clear()

###############################################################################################################

if __name__ == "__main__":
    try: 
    
        show_documents()
        find_with_id(choice(ids1_list))
        same_pet()
        same_letter_at_start()
        young_scientist()
    except TimeoutError as e:
        print(e)