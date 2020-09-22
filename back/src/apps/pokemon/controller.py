import requests

url = "https://pokeapi.co/api/v2/"


def get_pokemon(name):

    return requests.get("{}pokemon/{}".format(url, name))


def get_all(page):
    offset = (page - 1) * 20
    res = requests.get("{}pokemon?offset={}&limit=20".format(url, offset)).json()
    res.pop("next")
    res.pop("previous")
    return res


def get_type(type_pokemon):

    return requests.get("{}type/{}".format(url, type_pokemon))


def get_habilidad(type_pokemon):

    return requests.get("{}ability/{}".format(url, type_pokemon))

