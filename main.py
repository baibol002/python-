
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


hero1 = Hero("Артур", 5, 100, 20)
hero2 = Hero("Дракон", 10, 200, 50)

for hero in [hero1, hero2]:
    print("\n--- Новый герой ---")
    print(f"До действий: здоровье = {hero.health}, сила = {hero.strength}")

    hero.greet()
    hero.attack()
    hero.rest()

    print(f"После действий: здоровье = {hero.health}, сила = {hero.strength}")
