from project_2.pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        filtered_pokemons = [p for p in self.pokemon if p == pokemon]
        if filtered_pokemons:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        filtered_pokemons = [p for p in self.pokemon if p.name == pokemon_name]
        if filtered_pokemons:
            pokemon = filtered_pokemons[0]
            self.pokemon.remove(pokemon)
            return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for pokemon in self.pokemon:
            result += f"- {pokemon.name} with health {pokemon.health}\n"
        return result




