import random
from faker import Faker

fake = Faker()

def valid_creds_randomizer():
    name = fake.name()
    email = f'pavel_zelenskiy_25_{random.randint(100, 999)}@yandex.ru'
    password = f'{random.randint(100000, 999999)}'
    return name, email, password

def password_length_less_six_creds_randomizer():
    name = fake.name()
    email = f'pavel_zelenskiy_25_{random.randint(100, 999)}@yandex.ru'
    password = f'{random.randint(10000, 99999)}'
    return name, email, password