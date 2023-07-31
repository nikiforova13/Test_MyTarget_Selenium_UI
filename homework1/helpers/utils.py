from russian_names import RussianNames
from random import randint
from phone_gen import PhoneNumber


def generate_data(self):
    data = {}
    data["name"] = RussianNames().get_person()
    data["phone"] = PhoneNumber("Russia").get_number()
    data["Inn"] = randint(1000000000, 500000000000)
    return data
