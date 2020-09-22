from flask import jsonify

from src.apps.authentication.api import LoginView
from src.apps.pokemon.api import PokemonView
from src.apps.user.api import UserView
from src.views import app
import requests


@app.route('/')
def index():

    return jsonify({"info": "Por favor registrese en el sistema"})


UserView.register(app)
PokemonView.register(app)
LoginView.register(app)

if __name__ == "__main__":
    app.run(debug=True, port=4201, host="127.0.0.1")

