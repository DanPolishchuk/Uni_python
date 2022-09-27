import shelve
class RPG_character():
    def __init__(self, name, HP, race, fighting_style, side, inventory):
        self.name = name
        self.HP = HP
        self.race = race
        self.fighting_style = fighting_style
        self.side = side
        self.inventory = inventory

    def save(self):
        with shelve.open("c:/lab4/specs", "c") as specs:
            specs["Name"] = input("Name: ")
            specs["HP"] = input("HP: ")
            specs["Race"] = input("Race: ")
            specs["Fighting_style"] = input("Fighting_style: ")
            specs["Side"] = input("Side: ")
            specs["Inventory"] = [input("Main weapon: "), input("Additional weapon: "), input("Armor: ")]
    def load(self):
        print("\nLast save:\n")
        with shelve.open("c:/lab4/specs", "r") as specs:
            for key in specs:
                print(key, " - ", specs[key])
        with shelve.open("c:/lab4/specs", "n") as specs:
            specs["Name"] = input("\nType new specs:\nName: ")
            specs["HP"] = input("HP: ")
            specs["Race"] = input("Race: ")
            specs["Fighting_style"] = input("Fighting_style: ")
            specs["Side"] = input("Side: ")
            specs["Inventory"] = [input("Main weapon: "), input("Additional weapon: "), input("Armor: ")]
        print("\nNew save:\n")
        with shelve.open("c:/lab4/specs", "r") as specs:
            for key in specs:
                print(key, " - ", specs[key])
    def clear(self):
        with shelve.open("c:/lab4/specs", "n") as specs:
            specs.clear()
RPG_character.clear(RPG_character("", "", "", "", "", ""))
