import random
class Mammals:
    def __init__(self, kind, height, weight, haircolor, eyecolor):
        self.height = height
        self.weight = weight
        self.haircolor = haircolor
        self.eyecolor = eyecolor
        self.kind = kind
    def sleep(self):
        if self.kind != "Людина":
            print("Відновив сили в норі")
    def eat(self):
        if self.kind != "Людина":
            print("Вполював та з'їв здобич")
    def walk(self):
        if self.kind != "Людина":
            print("Вийшов на перевірку території")
class Person(Mammals):
    def info(self, name, gender):
        self.name = name
        self.gender = gender
        self.__mood = 0
    def sleep(self):
        Mammals.sleep(self)
        x = random.randint(0, 1)
        if x == 0:
            self.__mood = self.__mood + 5
            print("Солодко поспав на ліжечку")
        else:
            self.__mood = self.__mood - 6
            print("Наснився поганий сон")
    def eat(self):
        Mammals.eat(self)
        x = random.randint(0, 1)
        if x == 0:
            self.__mood = self.__mood + 7
            print("Приготував вдома перекус та втамував голод")
        else:
            self.__mood = self.__mood - 5
            print("Не було часу щоб перекусити")
    def walk(self):
        Mammals.eat(self)
        x = random.randint(0, 1)
        if x == 0:
            self.__mood = self.__mood + 3
            print("Вийшов на прогулянку з друзями та гарно провів час")
        else:
            self.__mood = self.__mood - 4
            print("Вийшов на вулицю та захворів")
    def mood(self):
        if self.__mood in range(-15, -9):
            print("Зараз", self.name, "має жахливий настрій")
        elif self.__mood in range(-9, -4):
            print("Зараз", self.name, "має поганий настрій")
        elif self.__mood in range(-4, 0):
            print("Зараз", self.name, "має сумний настрій")
        elif self.__mood in range(0, 6):
            print("Зараз", self.name, "має нормальний настрій")
        elif self.__mood in range(6, 11):
            print("Зараз", self.name, "має гарний настрій")
        elif self.__mood in range(11, 16):
            print("Зараз", self.name, "має чудовий настрій")
Dan = Person("Людина", 192, 82, "світло-русяве", "блакитні")
Dan.info("Даня", "чоловік")
Dan.mood()
Dan.eat()
Dan.sleep()
Dan.walk()
Dan.mood()