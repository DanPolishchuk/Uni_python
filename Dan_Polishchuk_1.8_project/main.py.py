import random; from time import *
list1 = ["Gold", "Red", "Brown"]


class Animal:
    def __init__(self, weight, wingspan, color):
        self.weight = weight; self.wingspan = wingspan; self.color = color


class Dragon(Animal):
    def __init__(self, weight, wingspan, color,):
        Animal.__init__(self, weight, wingspan, color)
        self.name = "Dragon"; self.special_ability = "Flying"
        a = abs(self.weight / 150 - 1); b = 1; c = abs(self.wingspan / 50 - 1)
        if self.color != "Gold":
            b = 0
        if self.wingspan < 30:
            c = 1
        self.price = ((a + b + c) / 3) * 3000000


class Salamander(Animal):
    def __init__(self, weight, wingspan, color):
        Animal.__init__(self, weight, wingspan, color)
        self.name = "Salamander"; self.special_ability = "Resistance"
        a = abs(self.weight / 900 - 1); b = 1; c = abs(self.wingspan / 15 - 1)
        if self.weight > 1500 or self.weight < 300:
            a = 1
        if self.wingspan > 30 or self.wingspan < 10:
            c = 1
        self.price = ((a + b + c) / 3) * 1000000


class Dinosaur(Animal):
    def __init__(self, weight, wingspan, color):
        global c
        Animal.__init__(self, weight, wingspan, color)
        self.name = "Dinosaur"; self.special_ability = "Fast running"
        a = abs(self.weight / 3250 - 1); b = 1
        if self.weight < 1500:
            a = 1
        if self.color != "Brown":
            b = 0
        if self.wingspan == 0 or self.wingspan > 5:
            c = 1
        elif self.wingspan == 1:
            c = 0.5
        elif self.wingspan == 2:
            c = 0.25
        elif self.wingspan == 3:
            c = 0.5 / 3
        elif self.wingspan == 4:
            c = 0.25 / 2
        elif self.wingspan == 5:
            c = 0.1
        self.price = self.price = ((a + b + c) / 3) * 2200000


class Pussy(Animal):
    def __init__(self, weight, wingspan, color):
        Animal.__init__(self, weight, wingspan, color)
        self.name = "Cat"; self.special_ability = "Kawaii"; self.price = 5000


class Fabric:
    def create(self):
        self.weight = random.randint(100, 5000); self.wingspan = random.randint(0, 50)
        self.color = random.choice(list1)
        if self.color == "Red":
            self.animal = Salamander(self.weight, self.wingspan, self.color)
        elif self.weight <= 300 and self.color == "Red":
            self.animal = Salamander(self.weight, self.wingspan, self.color)
        elif self.weight <= 300 and self.color == "Red" and self.wingspan <= 5:
            self.animal = Salamander(self.weight, self.wingspan, self.color)
        else:
            if self.weight <= 300:
                self.animal = Dragon(self.weight, self.wingspan, self.color)
            elif self.weight <= 300 and self.wingspan <= 5:
                self.animal = Dragon(self.weight, self.wingspan, self.color)
            else:
                if self.wingspan <= 5:
                    self.animal = Dinosaur(self.weight, self.wingspan, self.color)
                else:
                    x = random.randint(1, 3)
                    if x == 1:
                        self.animal = Dragon(self.weight, self.wingspan, self.color)
                    if x == 2:
                        self.animal = Salamander(self.weight, self.wingspan, self.color)
                    if x == 3:
                        self.animal = Dinosaur(self.weight, self.wingspan, self.color)


class Customer(Fabric):
    def __init__(self):
         self.fabric = Fabric(); self.adapter = Adapter(); self.set = Set(); self.bill = 0

    def order(self):
        print("- Good day! Our farm welcomes you. We currently have dragons, dinosaurs and salamanders in our "
              "assortment.Would you like to order a pet?"), sleep(1)
        print("-It is also possible to purchase a set of several animals"), sleep(1)
        while True:
            print("1 set: 3 dragons and 2 dinosaurs\n2 set: 1 dragon, 1 salamander, 1 dinosaur"
                  "\n3 set: 7 cats\n4 set: create one random animal"), sleep(1)
            answer1 = int(input("Which of the 4 offers do you choose?"))
            if answer1 == 1:
                self.set.get_set1(), exit()
            elif answer1 == 2:
                self.set.get_set2(), exit()
            elif answer1 == 3:
                self.set.get_set3(), exit()
            elif answer1 == 4:
                print("- Great, then let's see which animal will hatch from the egg..."), sleep(0.5)
                print("1"), sleep(0.5), print("2"), sleep(0.5), print("3"), sleep(0.5)
                print("- Congratulations with: ")
                self.adapter.check()
                if self.adapter.animal.name == "Cat":
                    print("'- It's a mess!!! An epidemic of dragonvirus has started in the country.\nIt affects all "
                          "animals that have at least one of the parameters is in the range: weight 200-600 kg, "
                          "wingspan length: 20 - 40 m.\nThe disease is fatal, but we gave the animal medicine, "
                          "but now it turned into a cat")
                self.adapter.info()
                print("'", self.adapter.animal.name, "will become your best friend, they are very active and loving"
                      "play with your master. You won't regret it for a minute if "
                      "buy a pet in our farm)'"), sleep(1)
                print("- What have you decided? Will you buy? I must immediately warn that in case of refusal "
                      "(according to the rules of our farm) you have to pay a third of the cost of the "
                      "animal"), sleep(0.5)
                answer2 = input("Enter 'yes' or 'no' : ")
                if answer2 == "yes":
                    self.bill += self.adapter.animal.price
                    print("- Great, we wish you a good time)))"), sleep(0.5)
                    print("- Amount to be paid: ", round(self.bill), "UAH."), exit()
                if answer2 == "no":
                    self.bill += (self.adapter.animal.price/3)
                    print("- Sorry, your amount : ", round(self.bill)), sleep(0.5)
                    print("- Maybe try again and buy another pet?")
                    answer3 = input("Enter 'yes' or 'no' : ")
                    if answer3 == "no":
                        exit()
            elif answer1 == "no":
                print("- Sad(((, come back another time)))"), exit()


class Adapter(Fabric):
    def check(self):
        self.create()
        if self.weight in range(200, 601) or self.wingspan in range(20, 41):
            self.weight = random.randint(5, 12); self.wingspan = 0.5; self.color = random.choice(list1)
            self.animal = Pussy(self.weight, self.wingspan, self.color)

    def info(self):
        print("Kind: ", self.animal.name, "Weight: ", self.weight, "kg.", "Wingspan",
              self.wingspan, "meter.", "Colour:", self.color, ".Feature: ",
              self.animal.special_ability, ".Price:", round(self.animal.price), "UAH.")


class Set:
    def __init__(self):
        self.fabric = Fabric(); self.adapter = Adapter(); self.set1 = self.set2 = self.set3 = self.bill = 0

    def get_set1(self):
        while self.set1 != 3 or self.set2 != 2:
            self.fabric.create()
            if self.fabric.animal.name == "Dragon" and self.set1 != 3:
                self.set1 += 1; self.bill += self.fabric.animal.price
                print("Kind: ", self.fabric.animal.name, ".Weight: ", self.fabric.weight, "kg.", "Wingspan",
                      self.fabric.wingspan, "meters.", "Colour:", self.fabric.color, ".Feature: ",
                      self.fabric.animal.special_ability, ".Price:", round(self.fabric.animal.price), "UAH."), sleep(0.5)
            elif self.fabric.animal.name == "Dinosaur" and self.set2 != 2:
                self.set2 += 1; self.bill += self.fabric.animal.price
                print("Kind: ", self.fabric.animal.name, ".Weight: ", self.fabric.weight, "kg.", "Wingspan",
                      self.fabric.wingspan, "meters.", "Colour:", self.fabric.color, ".Feature: ",
                      self.fabric.animal.special_ability, ".Price:", round(self.fabric.animal.price), "UAH."), sleep(0.5)
            else:
                self.bill += (self.fabric.animal.price/3)
        print("Amount to be paid - ", round(self.bill), "UAH")

    def get_set2(self):
        while self.set1 != 1 or self.set2 != 1 or self.set3 != 1:
            self.fabric.create()
            if self.fabric.animal.name == "Dragon" and self.set1 == 0:
                self.set1 += 1; self.bill += self.fabric.animal.price
                print("Kind: ", self.fabric.animal.name, ".Weight: ", self.fabric.weight, "kg.", "Wingspan",
                      self.fabric.wingspan, "meters.", "Colour:", self.fabric.color, ".Feature: ",
                      self.fabric.animal.special_ability, ".Price:", round(self.fabric.animal.price),
                      "UAH."), sleep(0.5)
            elif self.fabric.animal.name == "Dinosaur" and self.set2 == 0:
                self.set2 += 1; self.bill += self.fabric.animal.price
                print("Kind: ", self.fabric.animal.name, ".Weight: ", self.fabric.weight, "kg.", "Wingspan",
                      self.fabric.wingspan, "meters.", "Colour:", self.fabric.color, ".Feature: ",
                      self.fabric.animal.special_ability, ".Price:", round(self.fabric.animal.price), "UAH."), sleep(0.5)
            elif self.fabric.animal.name == "Salamander" and self.set3 == 0:
                self.set3 += 1; self.bill += self.fabric.animal.price
                print("Kind: ", self.fabric.animal.name, ".Weight: ", self.fabric.weight, "kg.", "Wingspan",
                      self.fabric.wingspan, "meters.", "Colour:", self.fabric.color, ".Feature: ",
                      self.fabric.animal.special_ability, ".Price:", round(self.fabric.animal.price), "UAH."), sleep(0.5)
            else:
                self.bill += (self.fabric.animal.price/3)
        print("Amount to be paid - ", round(self.bill), "UAH")

    def get_set3(self):
        while self.set1 != 7:
            self.adapter.check()
            if self.adapter.animal.name == "Cat":
                self.set1 += 1; self.bill += self.adapter.animal.price
                print("Kind: ", self.adapter.animal.name, ".Weight: ", self.adapter.weight, "kg.",
                      "Wingspan", self.adapter.wingspan, "meters.", "Colour:", self.adapter.color,
                      ".Feature: ", self.adapter.animal.special_ability, ".Price:",
                      round(self.adapter.animal.price), "UAH."), sleep(0.5)
            else:
                self.bill += (self.adapter.animal.price/3)
        print("Amount to be paid - ", round(self.bill), "UAH")
Dan = Customer(); Dan.order()
