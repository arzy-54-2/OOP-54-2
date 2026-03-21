from abc import ABC, abstractmethod

class Hero(ABC):

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1
        print(f" Здоровье {self.name} {self.__health}")
        print(" ")

    @abstractmethod
    def attack(self):
        pass


class Warrior(Hero):

    def attack(self):
        print("Воин атакует мечом")


class Mage(Hero):

    def attack(self):
        print("Маг использует магию")


class Assassin(Hero):

    def attack(self):
        print("Ассасин атакует из-под тишка")


warrior = Warrior("Thor", 5, 100, 20)
mage = Mage("Merlin", 7, 80, 15)
assassin = Assassin("Shadow", 6, 70, 25)

warrior.greet()
warrior.attack()
warrior.rest()

mage.greet()
mage.attack()
mage.rest()

assassin.greet()
assassin.attack()
assassin.rest()