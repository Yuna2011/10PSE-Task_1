import requests # Must import requests so we can use API

# API Base URL for F1 drivers
API_URL = "https://f1api.dev/api/current/drivers"

# Dictionary to store drivers
driver_list = {}

global name

def search_driver(name):
    """
    Search F1 driver by first name, last name, or full name.
    Works with any capitalization.
    Returns driver dictionary or None.
    """
    response = requests.get(API_URL)
    if response.status_code != 200:
        print("Could not retrieve driver data.")
        return None

    drivers = response.json()["drivers"]
    query = name.strip().lower()  

    for driver in drivers:
        first_name = driver["name"].strip().lower()
        last_name = driver["surname"].strip().lower()
        full_name = f"{first_name} {last_name}"

        if query == first_name or query == last_name or query == full_name:
            return {
                "name": driver["name"].title(),
                "surname": driver["surname"].title(),
                "birthday": driver["birthday"],
                "number": driver["number"],
                "team": driver["teamId"].title(),
                "nationality": driver["nationality"].title()
            }

    return None

def filter_drivers():
    while True: 
        print("\nFilter Menu:")
        print("1. Sort by teams")
        print("2. Sort by nationality")
        print("3. Back to main menu")
        choice = input("Choose an option: ")

        if choice == "1":  
            while True:  
                print("\n1. All teams")
                print("2. A specific team")
                print("3. Back to main menu")
                choice_team = input("Choose an option: ")

                if choice_team == "1":
                    response = requests.get(API_URL)
                    if response.status_code != 200:
                        print("Could not fetch drivers.\n")
                        break  

                    drivers = response.json()["drivers"]

                    teams = {}
                    for d in drivers:
                        team = d["teamId"].title()
                        if team not in teams:
                            teams[team] = []
                        teams[team].append(d)

                    print("\nAll teams and their drivers:")
                    for team_name, team_drivers in teams.items():
                        print(f"\nTeam: {team_name}")
                        for driver in team_drivers:
                            print(f"- {driver['name']} {driver['surname']} ({driver['number']})")
                    print("\n") 
                    break  


                elif choice_team == "2":
                    specific_team = input("Enter the team name: ")
                    response = requests.get(API_URL)
                    if response.status_code != 200:
                        print("Could not fetch drivers.\n")
                        break  

                    drivers = response.json()["drivers"]

                    team_drivers = [
                        d for d in drivers
                        if d["teamId"].lower() == specific_team.lower()
                    ]

                    if team_drivers:
                        print(f"\nDrivers in {specific_team}:")
                        for d in team_drivers:
                            print(f"- {d['name']} {d['surname']} ({d['number']})")
                    else:
                        print(f"\nNo drivers found for team {specific_team}.")

                    break
                elif choice_team == "3":
                    return  
                else:
                    print("\nInvalid choice. Try again.")

        elif choice == "2":
            print("\nWould you like to view all their nationalities or a nationality?")
            print("1. All nationalities")
            print("2. A specific nationality")
            choice_country = input("Choose an option: ")

            if choice_country == "1":  
                response = requests.get(API_URL)
                if response.status_code != 200:
                    print("Could not fetch drivers.\n")
                    break  

                drivers = response.json()["drivers"]

                countries = {}
                for d in drivers:
                    nationality = d["nationality"].title()  
                    if nationality not in countries:
                        countries[nationality] = []
                        countries[nationality].append(d)

                print("\nAll nationalities and their drivers:")
                for nat_name, nat_drivers in countries.items():
                    print(f"\nNationality: {nat_name}")
                    for driver in nat_drivers:
                        name = driver.get("name", "Unknown").title()
                        surname = driver.get("surname", "").title()
                        team = driver.get("teamId", "Unknown").title()
                        number = driver.get("number", "N/A")
                        print(f"- {name} {surname} ({team}, #{number})")
                    break

            elif choice_country == "2": 
                specific_country = input("\nEnter the name of the country: ")

                response = requests.get(API_URL)
                if response.status_code != 200:
                    print("Could not fetch drivers.\n")
                    break

                drivers = response.json()["drivers"]

                country_drivers = [
                    d for d in drivers
                    if d["nationality"].lower() == specific_country.lower()
                ]

                if country_drivers:
                    print(f"\nDrivers from {specific_country.title()}:")
                    for d in country_drivers:
                        name = d.get("name", "Unknown").title()
                        surname = d.get("surname", "Unknown").title()
                        team = d.get("teamId", "Unknown").title()
                        number = d.get("number", "N/A")
                        print(f"- {name} {surname} ({team}, #{number})")
                else:
                    print(f"\nNo drivers found from {specific_country.title()}.\n")

                break
            else:
                print("\nInvalid choice. Please try again.")

        elif choice == "3":
            return

        else:
            print("\nInvalid choice. Please try again.")
    
def manage_list():
     while True:
        print("\n1. View your driver list")
        print("2. Add a driver to you list")
        print("3. Remove a driver from your list")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            """Display all collected drivers."""
            if driver_list:
                for driver_name, details in driver_list.items():
                    print(f"{driver_name} - Name: {details['name']}, Birthday: {details['birthday']}, Number: {details['number']}, Team: {details['team']}, Nationality: {details['nationality']}")
            else:
                print("Your driver list is empty.")

        elif choice == "2":
            """Add a driver to the driver list."""
            name = input("\nEnter driver name to add: ")
            driver = search_driver(name)
            if driver:
                driver_list[driver["name"]] = driver
                print(f"{driver['name']} added to driver list.")

        elif choice == "3":
            """Remove a driver from the driver list."""
            name = input("\nEnter driver name to remove: ")
            if name.capitalize() in driver_list:
                del driver_list[name.capitalize()]
                print(f"{name.capitalize()} removed from driver list.")
            else:
                print("\nDriver not found in your driver list.")

        else:
            print("\nInvalid choice. Please try again.")


