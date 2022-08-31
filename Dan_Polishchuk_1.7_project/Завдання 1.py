class Person:
    def __init__(self, name, gender, mood):
        self.name = name
        self.gender = gender
        self.mood = mood
    def info(self):
        if self.gender == "жіночка":
            print("Привіт, мене звати", self.name, ",", "я - прекрасна", self.gender, ",", "сьогодні в мене", self.mood,
                  "настрій.")
        else:
            print("Привіт, мене звати", self.name, ",", "я - дивовижний", self.gender, ",", "сьогодні в мене", self.mood,
                  "настрій.")
Dan = Person("Даня", "чоловік", "неймовірний")
Lena = Person("Олена", "жіночка", "поганенький")
Kate = Person("Катерина", "жіночка", "нормальний")
Dan.info()
Lena.info()
Kate.info()