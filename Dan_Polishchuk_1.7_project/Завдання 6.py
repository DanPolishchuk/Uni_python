import random
class Money:
    def __init__(self):
        self.__sum = random.randint(10000, 100000)
        self.history = list()
    def replenishment(self):
        x = int(input("Введіть суму поповненння : "))
        self.__sum = self.__sum + x
        self.history.insert((0), "Поповнення, " + "+" + str(x) + " грн. " + "Баланс = " + str(self.__sum) + " грн.")
        print(self.history)
    def payment(self):
        y = int(input("Введіть суму оплати : "))
        if self.__sum < y:
            print("Недостатньо коштів на рахунку")
        else:
            z = input("Введіть призначення оплати : ")
            self.__sum = self.__sum - y
            self.history.insert((0), "Оплата: " + str(z) + " , " + "-" + str(y) + "грн. " + "Баланс = " + str(self.__sum) + "грн.")
            print(self.history)
    def balance(self):
        print("Баланс = ", self.__sum, "грн.")
class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.money = Money()
    def info(self):
        if self.gender == "жіночка":
            print("Привіт, мене звати", self.name, ",", "я - прекрасна", self.gender)
        else:
            print("Привіт, мене звати", self.name, ",", "я - дивовижний", self.gender)
    def get_replenishment(self):
        self.money.replenishment()
    def get_payment(self):
        self.money.payment()
    def get_balance(self):
        self.money.balance()
Dan = Person("Даня", "чоловік")
Dan.get_balance()
Dan.get_replenishment()
Dan.get_payment()
Dan.get_balance()

