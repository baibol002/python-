class Hero:
    def __init__(self, name, lvl, hp):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")

class MageHero(Hero):
    def __init__(self, name, lvl, hp, mp):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")

class WarriorHero(MageHero):
    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")

class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero, balance, password):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password):
        return self.__password == password

    @property
    def full_info(self):
        return (f"{self.hero.name} (уровень {self.hero.lvl}, HP: {self.hero.hp}) "
                f"| Баланс: {self._balance} SOM")

    def get_bank_name(self):
        return self.bank_name

    def bonus_for_level(self):
        return self.hero.lvl * 10

    def __str__(self):
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if type(self.hero) is not type(other.hero):
            raise TypeError("Нельзя сложить счета героев разных классов!")
        return self._balance + other._balance

    def __eq__(self, other):
        return type(self.hero) is type(other.hero) and self.hero.lvl == other.hero.lvl





mage1 = MageHero("Merlin", 50, 100, 150)
mage2 = MageHero("Merlin", 50, 100, 150)
warrior = WarriorHero("Conan", 50, 200, 0)

mage1.action()
warrior.action()

acc1 = BankAccount(mage1, 5000, "1234")
acc2 = BankAccount(mage2, 3000, "1234")
acc3 = BankAccount(warrior, 4000, "5678")

print(acc1)
print(acc2)

print("Банк:", acc1.get_bank_name())
print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

print("\n=== Проверка __add__ ===")
print("Сумма счетов двух магов:", acc1 + acc2)

try:
    print("Сумма мага и воина:", acc1 + acc3)
except TypeError as e:
    print("Ошибка:", e)

print("\n=== Проверка __eq__ ===")
print("Mage1 == Mage2 ?", acc1 == acc2)
print("Mage1 == Warrior ?", acc1 == acc3)