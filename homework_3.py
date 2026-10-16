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


warrior = Warrior("Артур", 10, 100, 50)
mage = Mage("Мерлин", 12, 70, 30)
assassin = Assassin("Тень", 11, 80, 40)

for hero in (warrior, mage, assassin):
    hero.greet()
    hero.attack()
    hero.rest()
    print()