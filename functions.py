import requests # Must import requests so we can use API

# API Base URL for PokéAPI
API_URL = "https://f1api.dev/api/current/drivers"

# Dictionary to store collected Pokémon
pokedex = {}

def search_pokemon(name):
    """Search for a Pokémon by name or ID and return its details.""" # Triple quotes is a docstring - allows multiline comments!
    response = requests.get(f"{API_URL}{name.lower()}")
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"].capitalize(),
            "id": data["id"],
            "height": data["height"],
            "weight": data["weight"],
            "types": [t["type"]["name"] for t in data["types"]]
        }
    else:
        print("Pokémon not found.")
        return None

def add_pokemon(name):
    """Add a Pokémon to the Pokédex."""
    pokemon = search_pokemon(name)
    if pokemon:
        pokedex[pokemon["name"]] = pokemon
        print(f"{pokemon['name']} added to Pokédex.")

def view_pokedex():
    """Display all collected Pokémon."""
    if pokedex:
        for name, details in pokedex.items():
            print(f"{name} - ID: {details['id']}, Height: {details['height']}, Weight: {details['weight']}, Types: {', '.join(details['types'])}")
    else:
        print("Your Pokédex is empty.")

def remove_pokemon(name):
    """Remove a Pokémon from the Pokédex."""
    if name.capitalize() in pokedex:
        del pokedex[name.capitalize()]
        print(f"{name.capitalize()} removed from Pokédex.")
    else:
        print("Pokémon not found in your Pokédex.")
