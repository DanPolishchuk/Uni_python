class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def info(self):
        if self.gender == "жіночка":
            print("Привіт, мене звати", self.name, ",", "я - прекрасна", self.gender)
        else:
            print("Привіт, мене звати", self.name, ",", "я - дивовижний", self.gender)
    def __del__(self):
        print(self.name, "видаленний з пам'яті")
Dan = Person("Даня", "чоловік")
Dan1 = Person("Даня", "чоловік")
Dan.info()
del Dan