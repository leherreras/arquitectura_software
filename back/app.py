from flask import url_for, redirect

from src.apps.authentication.api import LoginView
from src.apps.pokemon.api import PokemonView
from src.apps.user.api import UserView
from src.views import app


@app.route('/')
def index():
    return redirect(url_for('PokemonView:pokemons'))


UserView.register(app)
PokemonView.register(app, route_base='/')
LoginView.register(app)

if __name__ == "__main__":
    app.run(debug=True, port=4201, host="127.0.0.1")
