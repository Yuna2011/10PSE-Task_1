from functions import* # Import all functions from functions.py

def main(): # Main menu function
    while True: # Main menu loop
        print("\nF1 Menu:") # Displayed main menu
        print("1. Search Driver") # Search for a driver
        print("2. Filter Drivers") # Filter drivers by team or nationality
        print("3. Manage your list") # View, add, or remove drivers from your list
        print("4. Exit") # Exit the program
        choice = input("Choose an option: ") # Getting the user's choice

        if choice == "1": # Search Driver
            while True: # Loop for sub-menu
                print("\n1. Search for a driver") # Search for a driver
                print("2. HELP!") # Display help information
                print("3. Back to main menu") # Back to main menu
                sub_choice = input("Choose an option: ") # Getting the user's choice

                if sub_choice == "1": # Search for a driver
                    name = input("\nEnter driver name: ") # Getting the driver's name
                    driver = search_driver(name) # Searching for the driver
                    if driver:  # Driver was found
                        max_key_len = max(len(k) for k in driver) # Finding the maximum key length
                        for key, value in driver.items(): # Displaying driver information
                            print(f"{key:<{max_key_len}} : {value}") # Formatted output

                elif sub_choice == "2": # Display help information
                    print("""
Help Menu:
1. Searching for a driver
    - Enter the first name, surname or full name. No need to worry about capitalization.
    - Example: 'Charles', 'Leclerc', or 'Charles Leclerc' will all work.
                    """) # Help information for searching drivers

                elif sub_choice == "3": # Back to main menu
                    break # Exit the sub-menu loop and return to the main menu

                else: # Invalid choice
                    print("\nInvalid choice. Please try again.") # Display error message

        elif choice == "2": # Filter Drivers
            filter_drivers() # Filtering drivers by team or nationality
        elif choice == "3": # Manage your list
            manage_list() # Managing the user's list of drivers
        elif choice == "4": # Exit
            print("\n--- Final Interaction Log ---") # Displaying the final interaction log
            print(get_log()) # Displaying the interaction log
            print("\nThank you for using this program. Good Bye! :)") # Displaying exit message
            break # Exit the program
        else: # Invalid choice
            print("\nInvalid choice. Please try again.") # Display error message

if __name__ == "__main__": # Entry point of the program
    main() # Calling the main function to start the program