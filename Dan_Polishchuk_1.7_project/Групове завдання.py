import random
class Person:
    def __init__(self, name):
        self.name = name
        self.myday = MyDay()
    def morning(self):
        self.myday.event1()
    def breakfast(self):
        self.myday.event2()
    def way_to_work(self):
        self.myday.event3()
    def work(self):
        self.myday.event4()
    def evening(self):
        self.myday.event5()
    def mood(self):
        global x
        global y
        if self.myday.mood in range(-23, -12):
            x = "жахливий"
        elif self.myday.mood in range(-12, -5):
            x = "поганий"
        elif self.myday.mood in range(-5, 5):
            x = "нормальний"
        elif self.myday.mood in range(5, 12):
            x = "гарний"
        elif self.myday.mood in range(12, 23):
            x = "чудовий"
        if self.myday.health in range(-12, -4):
            y = "ненайкраще"
        elif self.myday.health in range(-4, 4):
            y = "нормальне"
        elif self.myday.health in range(4, 12):
            y = "добре"
        print(self.name, " має зараз ", x, "настрій та ", y, " самопочуття")
        print(self.name, "наразі має при собі", self.myday.money, "грн")
class MyDay:
    def __init__(self):
        self.mood = 0
        self.health = 0
        self.money = 10000
        self.__action1 = ["Прокинувся після солодкого 8-годинного сну",
                          "Всю ніч розважався у нічному клубі", "Прикинувся в поганому настрої після нічних кошмарів"]
        self.__action2 = ["Поснідав вівсянкою зі свіжими ягодами", "Похапцем з'їв тост з джемом",
                          "Запізнювався на роботу та не встиг по'їсти зранку"]
        self.__action3 = ["Дорогою на роботу випив смачної кави в Starbucks",
                          "Запізнився на автобус та змушений був замовляти таксі",
                          "Поїхав на роботу на свому велосипеді та насолоджувався свіжим повітрям"]
        self.__action4 = ["На роботі виконав план на день та отримав похвалу від боса у виді премії",
                          "Не міг зконцентруватись та робочий день був не продуктивний",
                          "Босс був злий на тебе через спізнення та виписав штраф"]
        self.__action5 = ["Приїхавши до дому, замовив піцу та подивився свій улюблений серіал",
                          "Був дуже втомлений після роботи тому ліг спати не повечерявши",
                          "Коли їхав до дому, в метро вкрали гаманець"]
    def event1(self):
        print("День розпочався):")
        x = random.randint(0, 2)
        if x == 0:
            print(self.__action1[0])
            self.mood = self.mood + 3
            self.health = self.health + 4
        elif x == 1:
            print(self.__action1[1])
            self.mood = self.mood + 4
            self.health = self.health - 3
        else:
            print(self.__action1[2])
            self.mood = self.mood - 4
            self.health = self.health - 2
    def event2(self):
        x = random.randint(0, 2)
        if x == 0:
            print(self.__action2[0])
            self.mood = self.mood + 2
            self.health = self.health + 3
        elif x == 1:
            print(self.__action2[1])
            self.mood = self.mood + 1
            self.health = self.health - 1
        else:
            print(self.__action2[2])
            self.mood = self.mood - 3
            self.health = self.health - 3
    def event3(self):
        x = random.randint(0, 2)
        if x == 0:
            print(self.__action3[0])
            self.mood = self.mood + 4
            self.health = self.health - 1
            self.money = self.money - 100
            print("Гроші = ", self.money, "грн")
        elif x == 1:
            print(self.__action3[1])
            self.mood = self.mood - 2
            self.money = self.money - 500
            print("Гроші = ", self.money, "грн")
        else:
            print(self.__action3[2])
            self.mood = self.mood + 2
            self.health = self.health + 4
    def event4(self):
        x = random.randint(0, 2)
        if x == 0:
            print(self.__action4[0])
            self.mood = self.mood + 3
            self.money = self.money + 3000
            print("Гроші = ", self.money, "грн")
        elif x == 1:
            print(self.__action4[1])
            self.mood = self.mood - 3
        else:
            print(self.__action4[2])
            self.mood = self.mood - 5
            self.money = self.money - 1500
            print("Гроші = ", self.money, "грн")
    def event5(self):
        x = random.randint(0, 2)
        if x == 0:
            print(self.__action5[0])
            self.mood = self.mood + 3
            self.health = self.health - 1
            self.money = self.money - 200
            print("Гроші = ", self.money, "грн")
        elif x == 1:
            print(self.__action5[1])
            self.mood = self.mood - 1
            self.health = self.health - 1
        else:
            print(self.__action5[2])
            self.mood = self.mood - 5
            self.money = self.money - 7000
            print("Гроші = ", self.money, "грн")
        print("День закінчився(")
Dan = Person("Даня")
Dan.mood()
Dan.morning()
Dan.breakfast()
Dan.way_to_work()
Dan.work()
Dan.evening()
Dan.mood()