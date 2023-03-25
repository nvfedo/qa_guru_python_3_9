import datetime
from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: str
    subject: str
    hobbies: str
    image: str
    state: str
    city: str


test_user = User(
    first_name='Random',
    last_name='Randomov',
    email='random@random.ru',
    phone='0987654332',
    address='Moscow',
    birthday=date(1990, 12, 12),
    gender='Male',
    subject='Physics',
    hobbies='Reading',
    image='photo.jpg',
    state='Haryana',
    city='Panipat')
