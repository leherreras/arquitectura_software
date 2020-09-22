from flask import jsonify

from src.apps.authentication.api import LoginView
from src.apps.pokemon.api import PokemonView
from src.apps.user.api import UserView
from src.views import app
import requests


@app.route('/')
def index():

    return jsonify({"info": "Por favor registrese en el sistema"})


# POKEMON
# Abilities
@app.route('/ability')
def abilitys():
    url = "https://pokeapi.co/api/v2/ability"
    res = requests.get(url)
    return res.json()


@app.route('/ability/<parametro>')
def ability(parametro):
    url = "https://pokeapi.co/api/v2/ability/"
    res = requests.get(url + parametro)
    return res.json()


# Characteristics
@app.route('/characteristic')
def characteristics():
    url = "https://pokeapi.co/api/v2/characteristic"
    res = requests.get(url)
    return res.json()


@app.route('/characteristic/<parametro>')
def characteristic(parametro):
    url = "https://pokeapi.co/api/v2/characteristic/"
    res = requests.get(url + parametro)
    return res.json()


# Egg Groups
@app.route('/egg-group')
def eggGroups():
    url = "https://pokeapi.co/api/v2/egg-group"
    res = requests.get(url)
    return res.json()


@app.route('/egg-group/<parametro>')
def eggGroup(parametro):
    url = "https://pokeapi.co/api/v2/egg-group/"
    res = requests.get(url + parametro)
    return res.json()


# Genders
@app.route('/gender')
def genders():
    url = "https://pokeapi.co/api/v2/gender"
    res = requests.get(url)
    return res.json()


@app.route('/gender/<parametro>')
def gender(parametro):
    url = "https://pokeapi.co/api/v2/gender/"
    res = requests.get(url + parametro)
    return res.json()


# Growth Rates
@app.route('/growth-rate')
def growthRates():
    url = "https://pokeapi.co/api/v2/growth-rate"
    res = requests.get(url)
    return res.json()


@app.route('/growth-rate/<parametro>')
def growthRate(parametro):
    url = "https://pokeapi.co/api/v2/growth-rate/"
    res = requests.get(url + parametro)
    return res.json()


# Natures
@app.route('/nature')
def natures():
    url = "https://pokeapi.co/api/v2/nature"
    res = requests.get(url)
    return res.json()


@app.route('/nature/<parametro>')
def nature(parametro):
    url = "https://pokeapi.co/api/v2/nature/"
    res = requests.get(url + parametro)
    return res.json()


# Pokeathlon Stats
@app.route('/pokeathlon-stat')
def pokeathlonStats():
    url = "https://pokeapi.co/api/v2/pokeathlon-stat"
    res = requests.get(url)
    return res.json()


@app.route('/pokeathlon-stat/<parametro>')
def pokeathlonStat(parametro):
    url = "https://pokeapi.co/api/v2/pokeathlon-stat/"
    res = requests.get(url + parametro)
    return res.json()


# Pokemon
@app.route('/pokemon')
def pokemons():
    url = "https://pokeapi.co/api/v2/pokemon"
    res = requests.get(url)
    return res.json()


@app.route('/pokemon/<parametro>')
def pokemon(parametro):
    url = "https://pokeapi.co/api/v2/pokemon/"
    res = requests.get(url + parametro)
    return res.json()


# Pokemon Location Areas
@app.route('/pokemon-location/<parametro>')
def pokemonLocation(parametro):
    url = "https://pokeapi.co/api/v2/pokemon/" + parametro + "/encounters"
    res = requests.get(url)
    print(res.json())
    return res.json()


# Pokemon Colors
@app.route('/pokemon-color')
def pokemonColors():
    url = "https://pokeapi.co/api/v2/pokemon-color"
    res = requests.get(url)
    return res.json()


@app.route('/pokemon-color/<parametro>')
def pokemonColor(parametro):
    url = "https://pokeapi.co/api/v2/pokemon-color/"
    res = requests.get(url + parametro)
    return res.json()


# Pokemon Forms
@app.route('/pokemon-form')
def pokemonForms():
    url = "https://pokeapi.co/api/v2/pokemon-form"
    res = requests.get(url)
    return res.json()


@app.route('/pokemon-form/<parametro>')
def pokemonForm(parametro):
    url = "https://pokeapi.co/api/v2/pokemon-form/"
    res = requests.get(url + parametro)
    return res.json()


# Pokemon Habitats
@app.route('/pokemon-habitat')
def pokemonHabitats():
    url = "https://pokeapi.co/api/v2/pokemon-habitat"
    res = requests.get(url)
    return res.json()


@app.route('/pokemon-habitat/<parametro>')
def pokemonHabitat(parametro):
    url = "https://pokeapi.co/api/v2/pokemon-habitat/"
    res = requests.get(url + parametro)
    return res.json()


# Pokemon Shapes
@app.route('/pokemon-shape')
def pokemonShapes():
    url = "https://pokeapi.co/api/v2/pokemon-shape"
    res = requests.get(url)
    return res.json()


@app.route('/pokemon-shape/<parametro>')
def pokemonShape(parametro):
    url = "https://pokeapi.co/api/v2/pokemon-shape/"
    res = requests.get(url + parametro)
    return res.json()


# Pokemon Species
@app.route('/pokemon-species')
def pokemonSpeciess():
    url = "https://pokeapi.co/api/v2/pokemon-species"
    res = requests.get(url)
    return res.json()


@app.route('/pokemon-species/<parametro>')
def pokemonSpecies(parametro):
    url = "https://pokeapi.co/api/v2/pokemon-species/"
    res = requests.get(url + parametro)
    return res.json()


# Stats
@app.route('/stat')
def stats():
    url = "https://pokeapi.co/api/v2/stat"
    res = requests.get(url)
    return res.json()


@app.route('/stat/<parametro>')
def stat(parametro):
    url = "https://pokeapi.co/api/v2/stat/"
    res = requests.get(url + parametro)
    return res.json()


# Types
@app.route('/type')
def types():
    url = "https://pokeapi.co/api/v2/type"
    res = requests.get(url)
    return res.json()


@app.route('/type/<parametro>')
def typePokemon(parametro):
    url = "https://pokeapi.co/api/v2/type/"
    res = requests.get(url + parametro)
    return res.json()


# berrys
@app.route('/berry')
def berrys():
    url = "https://pokeapi.co/api/v2/berry"
    res = requests.get(url)
    return res.json()


@app.route('/berry/<berry_id>')
def berry(berry_id):
    url = "https://pokeapi.co/api/v2/berry/"
    res = requests.get(url + berry_id)
    return res.json()


# berrys-firmnesses
@app.route('/berry-firmness/<berry_id>')
def berryFirmness(berry_id):
    url = "https://pokeapi.co/api/v2/berry-firmness/"
    res = requests.get(url + berry_id)
    return res.json()


# Berry Flavors
@app.route('/berry-flavor/<berry_id>')
def berryFlavor(berry_id):
    url = "https://pokeapi.co/api/v2/berry-flavor/"
    res = requests.get(url + berry_id)
    return res.json()


# Contest Types
@app.route('/contest-type')
def contestsType():
    url = "https://pokeapi.co/api/v2/contest-type/"
    res = requests.get(url)
    return res.json()


@app.route('/contest-type/<contest_id>')
def contestType(contest_id):
    url = "https://pokeapi.co/api/v2/contest-type/"
    res = requests.get(url + contest_id)
    return res.json()


# Contest Effect
@app.route('/contest-effect/<contest_id>')
def contestEffect(contest_id):
    url = "https://pokeapi.co/api/v2/contest-effect/"
    res = requests.get(url + contest_id)
    return res.json()


# Super Contest Effects
@app.route('/super-contest-effect/<contest_id>')
def superContestEffect(contest_id):
    url = "https://pokeapi.co/api/v2/super-contest-effect/"
    res = requests.get(url + contest_id)
    return res.json()


# Encounter Methods
@app.route('/encounter-method/<encounter_id>')
def encounterMethod(encounter_id):
    url = "https://pokeapi.co/api/v2/encounter-method/"
    res = requests.get(url + encounter_id)
    return res.json()


# Encounter Conditions
@app.route('/encounter-condition/<encounter_id>')
def encounterCondition(encounter_id):
    url = "https://pokeapi.co/api/v2/encounter-condition/"
    res = requests.get(url + encounter_id)
    return res.json()


# Encounter Condition Values
@app.route('/encounter-condition-value/<encounter_id>')
def encounterConditionValue(encounter_id):
    url = "https://pokeapi.co/api/v2/encounter-condition-value/"
    res = requests.get(url + encounter_id)
    return res.json()


# Evolution Chains
@app.route('/evolution-chain/<evolution_id>')
def evolutionChain(evolution_id):
    url = "https://pokeapi.co/api/v2/evolution-chain/"
    res = requests.get(url + evolution_id)
    return res.json()


# Evolution Triggers
@app.route('/evolution-trigger/<evolution_id>')
def evolutionTrigger(evolution_id):
    url = "https://pokeapi.co/api/v2/evolution-trigger/"
    res = requests.get(url + evolution_id)
    return res.json()


# Generations
@app.route('/generation/<generation_id>')
def generation(generation_id):
    url = "https://pokeapi.co/api/v2/generation/"
    res = requests.get(url + generation_id)
    return res.json()


# Pokedexes
@app.route('/pokedex/<pokedex_id>')
def pokedex(pokedex_id):
    url = "https://pokeapi.co/api/v2/pokedex/"
    res = requests.get(url + pokedex_id)
    return res.json()


# Version
@app.route('/version/<version_id>')
def version(version_id):
    url = "https://pokeapi.co/api/v2/version/"
    res = requests.get(url + version_id)
    return res.json()


# Version Groups
@app.route('/version-group/<version_id>')
def versionGroup(version_id):
    url = "https://pokeapi.co/api/v2/version-group/"
    res = requests.get(url + version_id)
    return res.json()


# ITEMS
# Item
@app.route('/item/<item_id>')
def item(item_id):
    url = "https://pokeapi.co/api/v2/item/"
    res = requests.get(url + item_id)
    return res.json()


# Item Attributes
@app.route('/item-attribute/<item_id>')
def itemAttribute(item_id):
    url = "https://pokeapi.co/api/v2/item-attribute/"
    res = requests.get(url + item_id)
    return res.json()


# Item Categories
@app.route('/item-category/<item_id>')
def itemCategory(item_id):
    url = "https://pokeapi.co/api/v2/item-category/"
    res = requests.get(url + item_id)
    return res.json()


# Item Fling Effects
@app.route('/item-fling-effect/<item_id>')
def itemFlingEffect(item_id):
    url = "https://pokeapi.co/api/v2/item-fling-effect/"
    res = requests.get(url + item_id)
    return res.json()


# Item Pockets
@app.route('/item-pocket/<item_id>')
def itemPocket(item_id):
    url = "https://pokeapi.co/api/v2/item-pocket/"
    res = requests.get(url + item_id)
    return res.json()


# LOCATIONS
# locations
@app.route('/location/<location>')
def location(location):
    url = "https://pokeapi.co/api/v2/location/"
    res = requests.get(url + location)
    return res.json()


# Location Areas
@app.route('/location-area/<location>')
def locationArea(location):
    url = "https://pokeapi.co/api/v2/location-area/"
    res = requests.get(url + location)
    return res.json()


# Pal Park Areas
@app.route('/pal-park-area/<location>')
def palParkArea(location):
    url = "https://pokeapi.co/api/v2/pal-park-area/"
    res = requests.get(url + location)
    return res.json()


# Regions
@app.route('/region/<region>')
def region(region):
    url = "https://pokeapi.co/api/v2/region/"
    res = requests.get(url + region)
    return res.json()


# MACHINES
# Machines
@app.route('/machine/<machine>')
def machine(machine):
    url = "https://pokeapi.co/api/v2/machine/"
    res = requests.get(url + machine)
    return res.json()


# MOVES
# Moves
@app.route('/move/<move>')
def move(move):
    url = "https://pokeapi.co/api/v2/move/"
    res = requests.get(url + move)
    return res.json()


# Move Ailments
@app.route('/move/<move>')
def moveAilment(move):
    url = "https://pokeapi.co/api/v2/move-ailment/"
    res = requests.get(url + move)
    return res.json()


# Move Battle Styles
@app.route('/move-battle-style/<move>')
def moveBattleStyle(move):
    url = "https://pokeapi.co/api/v2/move-battle-style/"
    res = requests.get(url + move)
    return res.json()


# Move Categories
@app.route('/move-category/<move>')
def moveCategory(move):
    url = "https://pokeapi.co/api/v2/move-category/"
    res = requests.get(url + move)
    return res.json()


# Move Damage Classes
@app.route('/move-damage-class/<move>')
def moveDamageClass(move):
    url = "https://pokeapi.co/api/v2/move-damage-class/"
    res = requests.get(url + move)
    return res.json()


# Move Learn Methods
@app.route('/move-learn-method/<move>')
def moveLearnMethod(move):
    url = "https://pokeapi.co/api/v2/move-learn-method/"
    res = requests.get(url + move)
    return res.json()


# Move Targets
@app.route('/move-target/<move>')
def moveTarget(move):
    url = "https://pokeapi.co/api/v2/move-target/"
    res = requests.get(url + move)
    return res.json()


@app.route('/general/<path:subpath>')
def general(subpath):
    res = requests.get(subpath)

    return res.json()


UserView.register(app)
PokemonView.register(app)
LoginView.register(app)

if __name__ == "__main__":
    app.run(debug=True, port=4201, host="127.0.0.1")

