import random

print("Домашнее задание №2")
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')

    def attack(self):
        self.strength = self.strength - 1
        return self.strength
    
    def rest(self):
        print(f'{self.name} отдыхает…')
        self.health = self.health + 1
        return self.health
    
class Warrior(Hero):
    def __init__(self, name, level, health, strength,stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"Воин {self.name} атакует мечом!")
        super.attack()

class Mage(Hero):
    def __init__(self, name, level, health, strength,  mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"Маг {self.name} кастует заклинание!")
        super.attack()

class Assassin(Hero):
    def __init__(self, name, level, health, strength ,stealth):
        super().__init__(name, level, health, strength)   
        self.stealth = stealth

    def attack(self):
        print(f"Ассасин {self.name} атакует из-под тишка!")
        super.attack()

kirito = Warrior("Kirito", 100, 1560, 180, 5)
asuna = Mage("Asuna", 99, 80, 100, 1000)
akemi = Assassin("Akemi", 101, 1000, 888, 999)

print("Выберите своего героя")
heronm= int(input("Warrior(1) / Mage(2) / Assassin(3): "))
if heronm == 1:
    yhero = kirito
elif heronm == 2:
    yhero = asuna
elif heronm == 3:
    yhero = akemi
else:
    print("Ошибка, повторите ввод :)")
    exit()

print(f"Вы выбрали: {yhero.__class__.__name__}")

opponents = [kirito, asuna, akemi]
opponent = random.choice(opponents)
print(f"Противник: {opponent.__class__.__name__}")

if type(yhero) == type(opponent):
    print("Силы равны")
elif (type(yhero) == Warrior or type(opponent) == Warrior) and (type(opponent) == Assassin  or type(yhero) == Assassin):
    print("Воин победил!")
elif (type(yhero) == Mage or type(opponent) == Mage) and (type(opponent) == Assassin  or type(yhero) == Assassin):
    print("Ассасин победил!")
elif (type(yhero) == Warrior or type(opponent) == Warrior) and (type(opponent) == Mage  or type(yhero) == Mage):
    print("Mage победил!")
else:
    print("Битва не состоялась")