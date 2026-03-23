import requests # Must import requests so we can use API
import pandas as pd
from datetime import datetime

# API Base URL for F1 drivers
API_URL = "https://f1api.dev/api/current/drivers"

# Create empty DataFrame
interaction_log = pd.DataFrame(columns=["time", "action", "input", "result"])

# Dictionary to store drivers
driver_list = {}

global name

def log_interaction(action, user_input, result):
    global interaction_log
    new_entry = {
        "time": datetime.now(),
        "action": action,
        "input": user_input,
        "result": result
    }
    interaction_log.loc[len(interaction_log)] = [datetime.now(), action, user_input, result]

def get_log():
    """Return the current interaction log"""
    return interaction_log

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
            log_interaction("search", name, "found")
            return {
                "name": driver["name"].title(),
                "surname": driver["surname"].title(),
                "birthday": driver["birthday"],
                "number": driver["number"],
                "team": driver["teamId"].title(),
                "nationality": driver["nationality"].title()
            }

            # If no driver matched after checking all
    print(f"Driver '{name}' not found.")
    log_interaction("search", name, "not found")
    return None

def filter_drivers():
    while True: 
        print("\nFilter Menu:")
        print("1. Sort by teams")
        print("2. Sort by nationality")
        print("3. HELP!")
        print("4. Back to main menu")
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
                    log_interaction("filter_team", "all_teams", "viewed")
                    break

                elif choice_team == "2":
                    specific_team = input("""\nEnter the team name out of 
- Ferrari
- Mercedes
- Red_Bull
- Alpine
- Haas
- Williams
- Rb
- Audi
- Cadillac
- Aston_Martin
: """)
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
                        log_interaction("filter_team", specific_team.title(), "viewed")
                    else:
                        print(f"\nNo drivers found for team {specific_team}.")
                        log_interaction("filter_team", specific_team.title(), "not found")

                    break
                elif choice_team == "3":
                    return  
                else:
                    print("\nInvalid choice. Try again.")

        elif choice == "2":
            print("\nWould you like to view all their nationalities or a nationality?")
            print("1. All nationalities")
            print("2. A specific nationality")
            print("3. Back to main menu")
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
                log_interaction("filter_nationality", "all_nationalities", "viewed")

            elif choice_country == "2":
                specific_country = input("""\nEnter the name of the country
- Great Britain
- Germany
- France
- Italy
- Spain
- Netherlands
- Australia
- Argentina
- Brazil
- Canada
- Mexico
- Monaco
- Thailand
- Finland
: """)

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
                    log_interaction("filter_nationality", specific_country.title(), "viewed")
                else:
                    print(f"\nNo drivers found from {specific_country.title()}.\n")
                    log_interaction("filter_nationality", specific_country.title(), "not found")

            elif choice_country == "3":
                break

            else:
                print("\nInvalid choice. Please try again.")
        
        elif choice == "3":
            print("""
Help Menu:
1. Sort by team
    - When searching for a specific team, enter the name exactly as it appears in the list.
2. Sort by nationality : Organize drivers based on their nationalities.
    - When searching for a specific nationality, enter the name exactly as it appears in the list.
            """)

        elif choice == "4":
            return

        else:
            print("\nInvalid choice. Please try again.")
    
def manage_list():
     while True:
        print("\n1. View your driver list")
        print("2. Add a driver to your list")
        print("3. Remove a driver from your list")
        print("4. HELP!")
        print("5. Back to main menu")
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
                log_interaction("add_driver", name, "success")
            else:
                print(f"Driver {name} not found.")
                log_interaction("add_driver", name, "not found")

        elif choice == "3":
            """Remove a driver from the driver list."""
            name = input("\nEnter driver name to remove: ")
            if name.capitalize() in driver_list:
                del driver_list[name.capitalize()]
                print(f"{name.capitalize()} removed from driver list.")
                log_interaction("remove_driver", name, "success")
            else:
                print("\nDriver not found in your driver list.")
                log_interaction("remove_driver", name, "not found")

        elif choice == "4":
            print("""
Help Menu:
1. Adding a driver
    - Enter the first name, surname or full name. No need to worry about capitalization.
    - Example: 'Charles', 'Leclerc', or 'Charles Leclerc' will all work.
2. Removing a driver
    - Enter the first name, surname or full name. No need to worry about capitalization.
    - Example: 'Charles', 'Leclerc', or 'Charles Leclerc' will all work.
            """)

        elif choice == "5":
            break

        else:
            print("\nInvalid choice. Please try again.")