# ы термнале нужно ввести команду pip install faker для того что бы устоновить 
from faker import Faker

fake = Faker("ru_RU")

for i in range(1, 6):
    print(f"Пользователь {i}")
    print("Имя:", fake.name())
    print("Адрес:", fake.address())
    print("Email:", fake.email())
    print("Телефон:", fake.phone_number())
    print()