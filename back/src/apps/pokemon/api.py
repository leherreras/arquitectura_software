import requests
from flask import jsonify
from flask_classy import FlaskView, route


class PokemonView(FlaskView):

    # # POKEMON
    # # Abilities
    @route('/ability')
    def abilities(self):
        url = "https://pokeapi.co/api/v2/ability"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/ability/<parametro>')
    def ability(self, parametro):
        url = "https://pokeapi.co/api/v2/ability/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Characteristics
    @route('/characteristic')
    def characteristics(self):
        url = "https://pokeapi.co/api/v2/characteristic"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/characteristic/<parametro>')
    def characteristic(self, parametro):
        url = "https://pokeapi.co/api/v2/characteristic/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Egg Groups
    @route('/egg-group')
    def egg_groups(self):
        url = "https://pokeapi.co/api/v2/egg-group"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/egg-group/<parametro>')
    def egg_group(self, parametro):
        url = "https://pokeapi.co/api/v2/egg-group/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Genders
    @route('/gender')
    def genders(self):
        url = "https://pokeapi.co/api/v2/gender"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/gender/<parametro>')
    def gender(self, parametro):
        url = "https://pokeapi.co/api/v2/gender/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Growth Rates
    @route('/growth-rate')
    def growth_rates(self):
        url = "https://pokeapi.co/api/v2/growth-rate"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/growth-rate/<parametro>')
    def growth_rate(self, parametro):
        url = "https://pokeapi.co/api/v2/growth-rate/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Natures
    @route('/nature')
    def natures(self):
        url = "https://pokeapi.co/api/v2/nature"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/nature/<parametro>')
    def nature(self, parametro):
        url = "https://pokeapi.co/api/v2/nature/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Pokeathlon Stats
    @route('/pokeathlon-stat')
    def pokeathlon_stats(self):
        url = "https://pokeapi.co/api/v2/pokeathlon-stat"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/pokeathlon-stat/<parametro>')
    def pokeathlon_stat(self, parametro):
        url = "https://pokeapi.co/api/v2/pokeathlon-stat/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Pokemon
    @route('/pokemon')
    def pokemons(self):
        url = "https://pokeapi.co/api/v2/pokemon"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/pokemon/<parametro>')
    def pokemon(self, parametro):
        url = "https://pokeapi.co/api/v2/pokemon/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Pokemon Location Areas
    @route('/pokemon-location/<parametro>')
    def pokemon_socation(self, parametro):
        url = "https://pokeapi.co/api/v2/pokemon/" + parametro + "/encounters"
        res = requests.get(url)
        print(jsonify(res.json()))
        return jsonify(res.json())

    # Pokemon Colors
    @route('/pokemon-color')
    def pokemon_solors(self):
        url = "https://pokeapi.co/api/v2/pokemon-color"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/pokemon-color/<parametro>')
    def pokemon_solor(self, parametro):
        url = "https://pokeapi.co/api/v2/pokemon-color/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Pokemon Forms
    @route('/pokemon-form')
    def pokemon_forms(self):
        url = "https://pokeapi.co/api/v2/pokemon-form"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/pokemon-form/<parametro>')
    def pokemon_form(self, parametro):
        url = "https://pokeapi.co/api/v2/pokemon-form/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Pokemon Habitats
    @route('/pokemon-habitat')
    def pokemon_habitats(self):
        url = "https://pokeapi.co/api/v2/pokemon-habitat"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/pokemon-habitat/<parametro>')
    def pokemon_habitat(self, parametro):
        url = "https://pokeapi.co/api/v2/pokemon-habitat/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Pokemon Shapes
    @route('/pokemon-shape')
    def pokemon_shapes(self):
        url = "https://pokeapi.co/api/v2/pokemon-shape"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/pokemon-shape/<parametro>')
    def pokemon_shape(self, parametro):
        url = "https://pokeapi.co/api/v2/pokemon-shape/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Pokemon Species
    @route('/pokemon-species')
    def pokemon_speciess(self):
        url = "https://pokeapi.co/api/v2/pokemon-species"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/pokemon-species/<parametro>')
    def pokemon_species(self, parametro):
        url = "https://pokeapi.co/api/v2/pokemon-species/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Stats
    @route('/stat')
    def stats(self):
        url = "https://pokeapi.co/api/v2/stat"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/stat/<parametro>')
    def stat(self, parametro):
        url = "https://pokeapi.co/api/v2/stat/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # Types
    @route('/type')
    def types(self):
        url = "https://pokeapi.co/api/v2/type"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/type/<parametro>')
    def type_pokemon(self, parametro):
        url = "https://pokeapi.co/api/v2/type/"
        res = requests.get(url + parametro)
        return jsonify(res.json())

    # berrys
    @route('/berry')
    def berry(self):
        url = "https://pokeapi.co/api/v2/berry"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/berry/<berry_id>')
    def berry(self, berry_id):
        url = "https://pokeapi.co/api/v2/berry/"
        res = requests.get(url + berry_id)
        return jsonify(res.json())

    # berrys-firmnesses
    @route('/berry-firmness/<berry_id>')
    def berry_firmness(self, berry_id):
        url = "https://pokeapi.co/api/v2/berry-firmness/"
        res = requests.get(url + berry_id)
        return jsonify(res.json())

    # Berry Flavors
    @route('/berry-flavor/<berry_id>')
    def berry_flavor(self, berry_id):
        url = "https://pokeapi.co/api/v2/berry-flavor/"
        res = requests.get(url + berry_id)
        return jsonify(res.json())

    # Contest Types
    @route('/contest-type')
    def contests_type(self):
        url = "https://pokeapi.co/api/v2/contest-type/"
        res = requests.get(url)
        return jsonify(res.json())

    @route('/contest-type/<contest_id>')
    def contest_type(self, contest_id):
        url = "https://pokeapi.co/api/v2/contest-type/"
        res = requests.get(url + contest_id)
        return jsonify(res.json())

    # Contest Effect
    @route('/contest-effect/<contest_id>')
    def contest_effect(self, contest_id):
        url = "https://pokeapi.co/api/v2/contest-effect/"
        res = requests.get(url + contest_id)
        return jsonify(res.json())

    # Super Contest Effects
    @route('/super-contest-effect/<contest_id>')
    def super_contest_effect(self, contest_id):
        url = "https://pokeapi.co/api/v2/super-contest-effect/"
        res = requests.get(url + contest_id)
        return jsonify(res.json())

    # Encounter Methods
    @route('/encounter-method/<encounter_id>')
    def encounter_method(self, encounter_id):
        url = "https://pokeapi.co/api/v2/encounter-method/"
        res = requests.get(url + encounter_id)
        return jsonify(res.json())

    # Encounter Conditions
    @route('/encounter-condition/<encounter_id>')
    def encounter_condition(self, encounter_id):
        url = "https://pokeapi.co/api/v2/encounter-condition/"
        res = requests.get(url + encounter_id)
        return jsonify(res.json())

    # Encounter Condition Values
    @route('/encounter-condition-value/<encounter_id>')
    def encounter_condition_value(self, encounter_id):
        url = "https://pokeapi.co/api/v2/encounter-condition-value/"
        res = requests.get(url + encounter_id)
        return jsonify(res.json())

    # Evolution Chains
    @route('/evolution-chain/<evolution_id>')
    def evolution_chain(self, evolution_id):
        url = "https://pokeapi.co/api/v2/evolution-chain/"
        res = requests.get(url + evolution_id)
        return jsonify(res.json())

    # Evolution Triggers
    @route('/evolution-trigger/<evolution_id>')
    def evolution_trigger(self, evolution_id):
        url = "https://pokeapi.co/api/v2/evolution-trigger/"
        res = requests.get(url + evolution_id)
        return jsonify(res.json())

    # Generations
    @route('/generation/<generation_id>')
    def generation(self, generation_id):
        url = "https://pokeapi.co/api/v2/generation/"
        res = requests.get(url + generation_id)
        return jsonify(res.json())

    # Pokedexes
    @route('/pokedex/<pokedex_id>')
    def pokedex(self, pokedex_id):
        url = "https://pokeapi.co/api/v2/pokedex/"
        res = requests.get(url + pokedex_id)
        return jsonify(res.json())

    # Version
    @route('/version/<version_id>')
    def version(self, version_id):
        url = "https://pokeapi.co/api/v2/version/"
        res = requests.get(url + version_id)
        return jsonify(res.json())

    # Version Groups
    @route('/version-group/<version_id>')
    def version_group(self, version_id):
        url = "https://pokeapi.co/api/v2/version-group/"
        res = requests.get(url + version_id)
        return jsonify(res.json())

    # ITEMS
    # Item
    @route('/item/<item_id>')
    def item(self, item_id):
        url = "https://pokeapi.co/api/v2/item/"
        res = requests.get(url + item_id)
        return jsonify(res.json())

    # Item Attributes
    @route('/item-attribute/<item_id>')
    def item_attribute(self, item_id):
        url = "https://pokeapi.co/api/v2/item-attribute/"
        res = requests.get(url + item_id)
        return jsonify(res.json())

    # Item Categories
    @route('/item-category/<item_id>')
    def item_category(self, item_id):
        url = "https://pokeapi.co/api/v2/item-category/"
        res = requests.get(url + item_id)
        return jsonify(res.json())

    # Item Fling Effects
    @route('/item-fling-effect/<item_id>')
    def item_fling_effect(self, item_id):
        url = "https://pokeapi.co/api/v2/item-fling-effect/"
        res = requests.get(url + item_id)
        return jsonify(res.json())

    # Item Pockets
    @route('/item-pocket/<item_id>')
    def item_pocket(self, item_id):
        url = "https://pokeapi.co/api/v2/item-pocket/"
        res = requests.get(url + item_id)
        return jsonify(res.json())

    # LOCATIONS
    # locations
    @route('/location/<location>')
    def location(self, location):
        url = "https://pokeapi.co/api/v2/location/"
        res = requests.get(url + location)
        return jsonify(res.json())

    # Location Areas
    @route('/location-area/<location>')
    def location_area(self, location):
        url = "https://pokeapi.co/api/v2/location-area/"
        res = requests.get(url + location)
        return jsonify(res.json())

    # Pal Park Areas
    @route('/pal-park-area/<location>')
    def pal_park_area(self, location):
        url = "https://pokeapi.co/api/v2/pal-park-area/"
        res = requests.get(url + location)
        return jsonify(res.json())

    # Regions
    @route('/region/<region>')
    def region(self, region):
        url = "https://pokeapi.co/api/v2/region/"
        res = requests.get(url + region)
        return jsonify(res.json())

    # MACHINES
    # Machines
    @route('/machine/<machine>')
    def machine(self, machine):
        url = "https://pokeapi.co/api/v2/machine/"
        res = requests.get(url + machine)
        return jsonify(res.json())

    # MOVES
    # Moves
    @route('/move/<move>')
    def move(self, move):
        url = "https://pokeapi.co/api/v2/move/"
        res = requests.get(url + move)
        return jsonify(res.json())

    # Move Ailments
    @route('/move/<move>')
    def move_ailment(self, move):
        url = "https://pokeapi.co/api/v2/move-ailment/"
        res = requests.get(url + move)
        return jsonify(res.json())

    # Move Battle Styles
    @route('/move-battle-style/<move>')
    def move_battle_style(self, move):
        url = "https://pokeapi.co/api/v2/move-battle-style/"
        res = requests.get(url + move)
        return jsonify(res.json())

    # Move Categories
    @route('/move-category/<move>')
    def move_category(self, move):
        url = "https://pokeapi.co/api/v2/move-category/"
        res = requests.get(url + move)
        return jsonify(res.json())

    # Move Damage Classes
    @route('/move-damage-class/<move>')
    def move_damage_class(self, move):
        url = "https://pokeapi.co/api/v2/move-damage-class/"
        res = requests.get(url + move)
        return jsonify(res.json())

    # Move Learn Methods
    @route('/move-learn-method/<move>')
    def move_learn_method(self, move):
        url = "https://pokeapi.co/api/v2/move-learn-method/"
        res = requests.get(url + move)
        return jsonify(res.json())

    # Move Targets
    @route('/move-target/<move>')
    def move_target(self, move):
        url = "https://pokeapi.co/api/v2/move-target/"
        res = requests.get(url + move)
        return jsonify(res.json())

    @route('/general/<path:subpath>')
    def general(self, subpath):
        res = requests.get(subpath)

        return jsonify(res.json())
