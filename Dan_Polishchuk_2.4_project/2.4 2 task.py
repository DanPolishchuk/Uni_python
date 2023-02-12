import shelve


class RPG_character:
    def __init__(self, name, HP, race, fighting_style, side, inventory):
        self.name = input("Name: ")
        self.HP = input("HP: ")
        self.race = input("Race: ")
        self.fighting_style = input("Fighting_style: ")
        self.side = input("Side: ")
        self.inventory = [input("Main weapon: "), input("Additional weapon: "), input("Armor: ")]

    def save(self):
        with shelve.open("c:/lab4/specs", "c") as specs:
            specs["Name"] = self.name
            specs["HP"] = self.HP
            specs["Race"] = self.race
            specs["Fighting_style"] = self.fighting_style
            specs["Side"] = self.side
            specs["Inventory"] = self.inventory
        print(self.name, self.HP, self.race, self.fighting_style, self.side, self.inventory)

    def load(self):
        choice = input("Would you like to change specs: ")
        if choice == "yes":
            print("Enter new specs:")
            self.name = input("Name: ")
            self.HP = input("HP: ")
            self.race = input("Race: ")
            self.fighting_style = input("Fighting_style: ")
            self.side = input("Side: ")
            self.inventory = [input("Main weapon: "), input("Additional weapon: "), input("Armor: ")]
            RPG_character.save(self)

    def clear(self):
        with shelve.open("c:/lab4/specs", "n") as specs:
            specs.clear()


Character = RPG_character("", "", "", "", "", "")
Character.save()
Character.load()