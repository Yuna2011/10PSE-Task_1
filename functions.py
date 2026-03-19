import requests # Must import requests so we can use API

# API Base URL for F1 drivers
API_URL = "https://f1api.dev/api/current/drivers"

# Dictionary to store drivers
driver_list = {}

def search_driver(name):
    """Search for a driver by name or ID and return its details.""" # Triple quotes is a docstring - allows multiline comments!
#    response = requests.get(f"{API_URL}/{name.lower()}")
#    if response.status_code == 200:
#        data = response.json()
#        return {
#            "name": data["name"].capitalize(),
#            "birthday": data["birthday"],
#            "number": data["number"],
#            "team": data["teamID"],
#            "nationality": data["nationality"]
#        }
#    else:
#        print("Driver not found.")
#        return None
    
    """Search for a driver by name or ID and return its details."""

    # Normalize input: "Max Verstappen" → "max_verstappen"
    normalized = name.strip().lower().replace(" ", "_")

    response = requests.get(f"{API_URL}/{normalized}")

    if response.status_code == 200:
        data = response.json()
        return {
            "name": data["name"],
            "birthday": data["birthday"],
            "number": data["number"],
            "team": data["teamId"],
            "nationality": data["nationality"]
        }
    else:
        print("Driver not found.")
        return None
    
def filter_drivers():
    while True:
        print("What filter would you like to use?")
        print("1. Sort by teams ")
        print("2. Sort by nationality")
        choice = input("Choose an option: ")

        if choice == "1":
            print("Would you like to view all the teams or a specific team?")
            print("1. All teams")
            print("2. A specific team")
            choice_team = input("Chooce an option: ")

            if choice_team == "1":
                print("good")
            elif choice_team == "2":
                print("good2")
                #choice_specific_team = input("Enter a team name: ")
            else:
                print("Invalid choice. Please try again.")

        elif choice == "2":
            print("Would you like to view all their nationalities or a nationality?")
            print("1. All nationalities")
            print("2. A specific nationality")
            choice_country = input("Chooce an option: ")

            if choice_country == "1":
                print("good")
            elif choice_country == "2":
                print("good2")
                #choice_specific_country = input("Enter a country name: ")
            else:
                print("Invalid choice. Please try again.")

        else:
            print("Invalid choice. Please try again.")
    
def manage_list(name):
     while True:
        print("1. View your driver list")
        print("2. Add a driver to you list")
        print("3. Remove a driver from your list")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            """Display all collected drivers."""
            if driver_list:
                for name, details in driver_list.items():
                    print(f"{name} - ID: {details['id']}, Height: {details['height']}, Weight: {details['weight']}, Types: {', '.join(details['types'])}")
            else:
                print("Your driver list is empty.")

        elif choice == "2":
            """Add a driver to the driver list."""
            name = input("Enter driver name to add: ")
            driver = search_driver(name)
            if driver:
                driver_list[driver["name"]] = driver
                print(f"{driver['name']} added to driver list.")

        elif choice == "3":
            """Remove a driver from the driver list."""
            name = input("Enter driver name to add: ")
            if name.capitalize() in driver_list:
                del driver_list[name.capitalize()]
                print(f"{name.capitalize()} removed from driver list.")
            else:
                print("Driver not found in your driver list.")

        else:
            print("Invalid choice. Please try again.")


