import requests
from homework7 import settings
from mock.flask_mock import SURNAME_DATA

url = f"http://{settings.APP_HOST}:{settings.APP_PORT}"


def test():
    print(requests.get(url).text)


def test_add_get_user():
    resp = requests.post(f"{url}/add_user", json={"name": "Dima"})
    user_id_from_add = resp.json()["user_id"]

    resp = requests.get(f"{url}/get_user/Dima")
    user_id_from_get = resp.json()["user_id"]
    assert user_id_from_add == user_id_from_get


def test_add_existent_user():
    requests.post(f"{url}/add_user", json={"name": "Olga"})
    resp = requests.post(f"{url}/add_user", json={"name": "Olga"})
    assert resp.status_code == 400


def test_get_non_existent_user():
    resp = requests.get(f"{url}/get_user/LOVE")
    assert resp.status_code == 404


def test_with_age():
    requests.post(f"{url}/add_user", json={"name": "fake_user"})
    resp = requests.get(f"{url}/get_user/fake_user")
    age = resp.json()["age"]
    assert isinstance(age, int)
    assert 18 <= age <= 105

def test_has_surname():
    requests.post(f'{url}/add_user', json={'name': 'Olya'})
    # Данные можно получить напрямую из mock. Здесь мы просто заполнили нужными нам данными эту переменную и проверили.
    SURNAME_DATA['Olya'] = 'OLOLOEVA'

    resp = requests.get(f'{url}/get_user/Olya')
    surname = resp.json()['surname']
    assert surname == 'OLOLOEVA'


def test_has_no_surname():
    requests.post(f'{url}/add_user', json={'name': 'Sveta'})

    resp = requests.get(f'{url}/get_user/Sveta')
    surname = resp.json()['surname']
    assert surname == None