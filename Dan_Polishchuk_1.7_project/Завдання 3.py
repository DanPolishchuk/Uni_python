class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.__cash = 100000
    def replenishment(self):
        x = int(input("Введіть суму поповнення : "))
        self.__cash = self.__cash + x
        print("Ви поповнили рахунок на ", x, "гривень")
        return self.__cash
    def payment(self):
        y = int(input("Введіть суму оплати : "))
        self.__cash = self.__cash - y
        print("Ви оплатили на суму", y, "гривень")
        return self.__cash
    def balance(self):
        print(self.__cash, "- баланс")
    def info(self):
        if self.gender == "жіночка":
            print("Привіт, мене звати", self.name, ",", "я - прекрасна", self.gender)
        else:
            print("Привіт, мене звати", self.name, ",", "я - дивовижний", self.gender)
dan = Person("Даня", "чоловік")
dan.balance()
dan.replenishment()
dan.payment()
dan.balance()
