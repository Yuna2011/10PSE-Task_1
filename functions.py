import requests # Must import requests so we can use API

# API Base URL for PokéAPI
API_URL = "https://f1api.dev/api/current/drivers"

# Dictionary to store collected drivers
driver_list = {}

def search_driver(name):
    """Search for a driver by name or ID and return its details.""" # Triple quotes is a docstring - allows multiline comments!
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
        print("Driver not found.")
        return None

def add_driver(name):
    """Add a driver to the driver list."""
    driver = search_driver(name)
    if driver:
        driver_list[driver["name"]] = driver
        print(f"{driver['name']} added to driver list.")

def view_driver_list():
    """Display all collected drivers."""
    if driver_list:
        for name, details in driver_list.items():
            print(f"{name} - ID: {details['id']}, Height: {details['height']}, Weight: {details['weight']}, Types: {', '.join(details['types'])}")
    else:
        print("Your driver list is empty.")

def remove_driver(name):
    """Remove a driver from the driver list."""
    if name.capitalize() in driver_list:
        del driver_list[name.capitalize()]
        print(f"{name.capitalize()} removed from driver list.")
    else:
        print("Driver not found in your driver list.")
