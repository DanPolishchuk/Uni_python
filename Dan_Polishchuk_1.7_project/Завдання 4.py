class Mammals:
    def __init__(self, height, weight, haircolor, eyecolor):
        self.height = height
        self.weight = weight
        self.haircolor = haircolor
        self.eyecolor = eyecolor
    def sleep(self):
        print("Солодко поспав")
    def eat(self):
        print("Смачно поїв")
    def walk(self):
        print("Вийшов на прогулянку")
class Person(Mammals):
    def info(self, name, gender, mood):
        self.name = name
        self.gender = gender
        self.mood = mood
        if self.gender == "жіночка":
            print("Привіт, мене звати", self.name, ",", "я - прекрасна", self.gender, ",", "сьогодні в мене", self.mood,
                  "настрій.")
        else:
            print("Привіт, мене звати", self.name, ",", "я - дивовижний", self.gender, ",", "сьогодні в мене", self.mood,
                  "настрій.")
Dan = Person(192, 82, "світло-русяве", "блакитні")
Dan.info("Даня", "чоловік", "чудовий")
Dan.eat()
Dan.sleep()
Dan.walk()