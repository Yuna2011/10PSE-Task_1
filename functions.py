import requests # For making HTTP requests to the F1 API
import pandas as pd # Import the pandas library for data manipulation and analysis
from datetime import datetime # Import the datetime class for working with dates and times

API_URL = "https://f1api.dev/api/current/drivers" # API Base URL for F1 drivers

interaction_log = pd.DataFrame(columns=["time", "action", "input", "result"]) # Create empty DataFrame

driver_list = {} # Dictionary to store drivers

global name # Current driver name being searched

def log_interaction(action, user_input, result): # Log user interactions
    global interaction_log # Reference the global interaction log
    new_entry = { # Create a new log entry
        "time": datetime.now(), # Current timestamp
        "action": action, # User action
        "input": user_input, # User input
        "result": result # Result of the action
    }
    interaction_log.loc[len(interaction_log)] = [datetime.now(), action, user_input, result] # Add the new entry to the log

def get_log(): # Get the current interaction log
    return interaction_log # Return the interaction log

def search_driver(name): # Search for a driver by name
    response = requests.get(API_URL) # Make a request to the API
    if response.status_code != 200: # Check if the request was successful
        print("Could not retrieve driver data.") # Log the error
        return None # Return None if the request failed

    drivers = response.json()["drivers"] # Get the list of drivers
    query = name.strip().lower() # Normalize the query

    for driver in drivers: # Iterate through the list of drivers
        first_name = driver["name"].strip().lower() # Get the driver's first name
        last_name = driver["surname"].strip().lower() # Get the driver's last name
        full_name = f"{first_name} {last_name}" # Get the driver's full name

        if query == first_name or query == last_name or query == full_name: # Check for a match
            log_interaction("search", name, "found") # Log the successful search
            return { # Return the driver information
                "name": driver["name"].title(), # Driver's full name
                "surname": driver["surname"].title(), # Driver's surname
                "birthday": driver["birthday"], # Driver's birthday
                "number": driver["number"], # Driver's number
                "team": driver["teamId"].title(), # Driver's team
                "nationality": driver["nationality"].title() # Driver's nationality
            }

    print(f"Driver '{name}' not found.") # Log the unsuccessful search
    log_interaction("search", name, "not found") # Log the unsuccessful search
    return None # Return None if no driver was found

def filter_drivers(): # Function to filter drivers
    while True: # Keep the filter menu active
        print("\nFilter Menu:") # Display the filter menu
        print("1. Sort by teams") # Option to sort drivers by their teams
        print("2. Sort by nationality") # Option to sort drivers by their nationality
        print("3. HELP!") # Option to display help information
        print("4. Back to main menu") # Option to go back to the main menu
        choice = input("Choose an option: ") # Get user input for menu choice

        if choice == "1": # Sort by teams
            while True: # Keep the sort by teams menu active
                print("\n1. All teams") # Option to view all teams
                print("2. A specific team") # Option to view a specific team
                print("3. Back to main menu") # Option to go back to the main menu
                choice_team = input("Choose an option: ") # Get user input for team choice

                if choice_team == "1": # View all teams
                    response = requests.get(API_URL) # Fetch all drivers
                    if response.status_code != 200: # Check if the request was successful
                        print("Could not fetch drivers.\n") # Log the error
                        break # Exit the loop if the request failed

                    drivers = response.json()["drivers"] # Get the list of drivers

                    teams = {} # Initialize a dictionary to hold teams and their drivers
                    for d in drivers: # Iterate through the list of drivers
                        team = d["teamId"].title() # Get the driver's team
                        if team not in teams: # If the team is not already in the dictionary
                            teams[team] = [] # Initialize the team entry
                        teams[team].append(d) # Add the driver to the team's list

                    print("\nAll teams and their drivers:") # Display all teams and their drivers
                    for team_name, team_drivers in teams.items(): # Iterate through the teams
                        print(f"\nTeam: {team_name}") # Display the team name
                        for driver in team_drivers: # Iterate through the drivers in the team
                            print(f"- {driver['name']} {driver['surname']} ({driver['number']})") # Display the driver's name and number
                    print("\n") # Log the viewing of all teams
                    log_interaction("filter_team", "all_teams", "viewed") # Log the interaction
                    break # Exit the loop after viewing all teams

                elif choice_team == "2": # View a specific team
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
: """) # Get user input for specific team
                    response = requests.get(API_URL) # Fetch all drivers
                    if response.status_code != 200: # Check if the request was successful
                        print("Could not fetch drivers.\n") # Log the error
                        break # Exit the loop if the request failed

                    drivers = response.json()["drivers"] # Get the list of drivers

                    team_drivers = [ # Get the drivers for the specific team
                        d for d in drivers # Iterate through the drivers
                        if d["teamId"].lower() == specific_team.lower() # Check if the driver belongs to the specific team
                    ] # End of list comprehension

                    if team_drivers: # Check if there are drivers for the specific team
                        print(f"\nDrivers in {specific_team}:") # Display the drivers in the specific team
                        for d in team_drivers: # Iterate through the drivers in the specific team
                            print(f"- {d['name']} {d['surname']} ({d['number']})") # Display the driver's name and number
                        log_interaction("filter_team", specific_team.title(), "viewed") # Log the interaction
                    else: # If no drivers found for the specific team
                        print(f"\nNo drivers found for team {specific_team}.") # Log the not found case
                        log_interaction("filter_team", specific_team.title(), "not found") # Log the interaction

                    break # Exit the loop after viewing the specific team
                elif choice_team == "3": # Go back to the main menu
                    return # Go back to the main menu
                else: # Invalid choice
                    print("\nInvalid choice. Try again.") # Log the invalid choice

        elif choice == "2": # View nationalities
            print("\nWould you like to view all their nationalities or a nationality?") # Ask for user input
            print("1. All nationalities") # View all nationalities
            print("2. A specific nationality") # View a specific nationality
            print("3. Back to main menu") # Go back to the main menu
            choice_country = input("Choose an option: ") # Get user input for nationality choice

            if choice_country == "1": # View all nationalities
                response = requests.get(API_URL) # Fetch all drivers
                if response.status_code != 200: # Check if the request was successful
                    print("Could not fetch drivers.\n") # Log the error
                    break # Exit the loop if the request failed

                drivers = response.json()["drivers"] # Get the list of drivers

                countries = {} # Map of nationalities to drivers
                for d in drivers: # Iterate through the drivers
                    nationality = d["nationality"].title() # Get the driver's nationality
                    if nationality not in countries: # If the nationality is not in the map
                        countries[nationality] = [] # Create a new list for the nationality
                    countries[nationality].append(d) # Add the driver to the nationality list

                print("\nAll nationalities and their drivers:") # Display all nationalities and their drivers
                for nat_name, nat_drivers in countries.items(): # Iterate through the nationalities
                    print(f"\nNationality: {nat_name}") # Display the nationality
                    for driver in nat_drivers: # Iterate through the drivers of the nationality
                        name = driver.get("name", "Unknown").title() # Get the driver's name
                        surname = driver.get("surname", "").title() # Get the driver's surname
                        team = driver.get("teamId", "Unknown").title() # Get the driver's team
                        number = driver.get("number", "N/A") # Get the driver's number
                        print(f"- {name} {surname} ({team}, #{number})") # Display the driver's information
                        break # Exit the loop after displaying the driver
                log_interaction("filter_nationality", "all_nationalities", "viewed") # Log the interaction

            elif choice_country == "2": # View a specific nationality
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
: """) # Get the specific nationality from the user

                response = requests.get(API_URL) # Fetch all drivers
                if response.status_code != 200: # Check if the request was successful
                    print("Could not fetch drivers.\n") # Log the error
                    break # Exit the loop if the request failed

                drivers = response.json()["drivers"] # Get the list of drivers

                country_drivers = [ # Get the drivers from the specific nationality
                    d for d in drivers # Iterate through the drivers
                    if d["nationality"].lower() == specific_country.lower() # Check if the nationality matches
                ] # End of list comprehension

                if country_drivers: # Check if there are drivers from the specific nationality
                    print(f"\nDrivers from {specific_country.title()}:") # Display the drivers from the specific nationality
                    for d in country_drivers: # Iterate through the drivers from the specific nationality
                        name = d.get("name", "Unknown").title() # Get the driver's name
                        surname = d.get("surname", "Unknown").title() # Get the driver's surname
                        team = d.get("teamId", "Unknown").title() # Get the driver's team
                        number = d.get("number", "N/A") # Get the driver's number
                        print(f"- {name} {surname} ({team}, #{number})") # Display the driver's information
                    log_interaction("filter_nationality", specific_country.title(), "viewed") # Log the interaction
                else: # No drivers found from the specific nationality
                    print(f"\nNo drivers found from {specific_country.title()}.\n") # Display the message
                    log_interaction("filter_nationality", specific_country.title(), "not found") # Log the interaction

            elif choice_country == "3": # Go back to the previous menu
                break # Exit the loop

            else: # Invalid choice
                print("\nInvalid choice. Please try again.") # Display the error message

        elif choice == "3": # Help
            print(""" 
Help Menu:
1. Sort by team
    - When searching for a specific team, enter the name exactly as it appears in the list.
2. Sort by nationality : Organize drivers based on their nationalities.
    - When searching for a specific nationality, enter the name exactly as it appears in the list.
            """) # Display the help information

        elif choice == "4": # Back to main menu
            return # Go back to the main menu

        else: # Invalid choice
            print("\nInvalid choice. Please try again.") # Display the error message

def manage_list(): # Manage the driver's list
     while True: # Keep the management menu active
        print("\n1. View your driver list") # Display the option to view the driver list
        print("2. Add a driver to your list") # Display the option to add a driver to the list
        print("3. Remove a driver from your list") # Display the option to remove a driver from the list
        print("4. HELP!") # Display the option for help
        print("5. Back to main menu") # Display the option to go back to the main menu
        choice = input("Choose an option: ") # Get the user's choice

        if choice == "1": # View driver list
            if driver_list: # Check if the driver list is not empty
                for driver_name, details in driver_list.items(): # Iterate through the driver list
                    print(f"{driver_name} - Name: {details['name']}, Birthday: {details['birthday']}, Number: {details['number']}, Team: {details['team']}, Nationality: {details['nationality']}") # Display driver information
            else: # No drivers found
                print("Your driver list is empty.") # Display the message

        elif choice == "2": # Add a driver to the driver list
            name = input("\nEnter driver name to add: ") # Get the driver's name
            driver = search_driver(name) # Search for the driver
            if driver: # Driver found
                driver_list[driver["name"]] = driver # Add driver to the list
                print(f"{driver['name']} added to driver list.") # Display success message
                log_interaction("add_driver", name, "success") # Log the interaction
            else: # Driver not found
                print(f"Driver {name} not found.") # Display error message
                log_interaction("add_driver", name, "not found") # Log the interaction

        elif choice == "3": # Remove a driver from the driver list
            name = input("\nEnter driver name to remove: ") # Get the driver's name
            if name.capitalize() in driver_list: # Check if driver is in the list
                del driver_list[name.capitalize()] # Remove driver from the list
                print(f"{name.capitalize()} removed from driver list.") # Display success message
                log_interaction("remove_driver", name, "success") # Log the interaction
            else: # Driver not found
                print("\nDriver not found in your driver list.") # Display error message
                log_interaction("remove_driver", name, "not found") # Log the interaction

        elif choice == "4": # Help menu
            print("""
Help Menu:
1. Adding a driver
    - Enter the first name, surname or full name. No need to worry about capitalization.
    - Example: 'Charles', 'Leclerc', or 'Charles Leclerc' will all work.
2. Removing a driver
    - Enter the first name, surname or full name. No need to worry about capitalization.
    - Example: 'Charles', 'Leclerc', or 'Charles Leclerc' will all work.
            """) # Display help information

        elif choice == "5": # Back to main menu
            break # Go back to the main menu

        else: # Invalid choice
            print("\nInvalid choice. Please try again.") # Display the error message