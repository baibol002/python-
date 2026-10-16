import random


class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print("Воин атакует мечом!")
        self.strength -= 1


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print("Маг кастует заклинание!")
        self.strength -= 1


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print("Ассасин атакует из-под тишка!")
        self.strength -= 1


warrior = Warrior("Артур", 5, 100, 20, 80)
mage = Mage("Мерлин", 7, 80, 25, 100)
assassin = Assassin("Тень", 6, 90, 30, 95)

heroes = {
    "warrior": warrior,
    "mage": mage,
    "assassin": assassin
}

choices = {
    "warrior": "Камень",
    "assassin": "Ножницы",
    "mage": "Бумага"
}

print("=== Герои ===")

for hero in heroes.values():
    hero.greet()
    hero.attack()
    hero.rest()
    print(
        f"Здоровье: {hero.health}, сила: {hero.strength}"
    )
    print()

print("Камень, ножницы, бумага")
print("Выберите героя: Warrior / Mage / Assassin")

while True:
    user_choice = input("Ваш выбор: ").strip().lower()

    if user_choice in heroes:
        break

    print("Неверный выбор. Введите Warrior, Mage или Assassin.")

opponent_choice = random.choice(list(heroes.keys()))

print(f"Вы выбрали: {user_choice.capitalize()}")
print(f"Противник: {opponent_choice.capitalize()}")

if user_choice == opponent_choice:
    print("Ничья!")
elif (
    (user_choice == "warrior" and opponent_choice == "assassin")
    or (user_choice == "assassin" and opponent_choice == "mage")
    or (user_choice == "mage" and opponent_choice == "warrior")
):
    print(f"{user_choice.capitalize()} победил!")
else:
    print(f"{opponent_choice.capitalize()} победил!")
