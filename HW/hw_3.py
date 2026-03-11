from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')

    def rest(self):
        print(f'{self.name} отдыхает…')
        self.__health = self.__health + 1
    
    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):

    def attack(self):
        print(f"Воин {self.name} атакует мечом!")
        self.strength = self.strength - 1
        

class Mage(Hero):

    def attack(self):
        print(f"Маг {self.name} использует магию!")
        self.strength = self.strength - 1
        

class Assassin(Hero):

    def attack(self):
        print(f"Ассасин {self.name} атакует из-под тишка!")
        self.strength = self.strength - 1
        
    
kirito = Warrior("Kirito", 100, 1560, 180)
asuna = Mage("Asuna", 99, 80, 100)
akemi = Assassin("Akemi", 101, 1000, 888)

kirito.greet()
kirito.attack()
kirito.rest()

asuna.greet()
asuna.attack()
asuna.rest()

akemi.greet()
akemi.attack()
akemi.rest()