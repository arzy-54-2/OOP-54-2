from abc import ABC, abstractmethod

class Hero(ABC):

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

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


# создание объектов
warrior = Warrior("Kratos", 1, 100, 10)
mage = Mage("Harry", 1, 80, 8)
assassin = Assassin("Ezio", 1, 90, 9)


# вызов методов
warrior.greet()
warrior.attack()
warrior.rest()

mage.greet()
mage.attack()
mage.rest()

assassin.greet()
assassin.attack()
assassin.rest()