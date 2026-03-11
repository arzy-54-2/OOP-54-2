print("Домашнее задание №1")
class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength
    def greet(self):
        print(f'Привет, я {self.name}, мой уровень {self.level}')
    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength = self.strength - 1
        return self.strength
    def rest(self):
        print(f'{self.name} отдыхает…')
        self.health = self.health + 1
        return self.health

kirito = Hero("Kirito", 100, 100, 100)
asuna = Hero("Asuna", 99, 98, 1000)

kirito.greet()
print(f'Сила: {kirito.strength}, Здоровье: {kirito.health}')
print(f'Сила {kirito.name} стала {kirito.attack()}')
print(f'Здоровье {kirito.name} стало {kirito.rest()}\n')

asuna.greet()
print(f'Сила: {asuna.strength}, Здоровье: {asuna.health}')
print(f'Сила {asuna.name} стала {asuna.attack()}')
print(f'Здоровье {asuna.name} стало {asuna.rest()}')