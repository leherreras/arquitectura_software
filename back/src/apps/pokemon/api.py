from flask import jsonify
from flask_classy import FlaskView

from src.apps.pokemon.controller import get_pokemon, get_type, get_habilidad, get_all


class PokemonView(FlaskView):

    def index(self):
        res = get_all(1)
        return jsonify(res)

    def todos(self, page):
        res = get_all(int(page))
        return jsonify(res)

    def get(self, name):
        res = get_pokemon(name)
        return jsonify(res.json())

    def tipo(self, type_pokemon):
        res = get_type(type_pokemon)
        return jsonify(res.json())

    def habilidad(self, type_pokemon):
        res = get_habilidad(type_pokemon)
        return jsonify(res.json())