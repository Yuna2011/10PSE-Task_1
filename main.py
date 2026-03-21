from functions import*
from functions import search_driver, filter_drivers, manage_list, interaction_log, log_interaction

def main():
    while True:
        print("\nF1 Menu:")
        print("1. Search Driver")
        print("2. Filter Drivers")
        print("3. Manage your list")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            while True:
                print("\n1. Search for a driver")
                print("2. HELP!")
                print("3. Back to main menu")
                sub_choice = input("Choose an option: ")

                if sub_choice == "1":
                    name = input("\nEnter driver name: ")
                    driver = search_driver(name)
                    if driver:  # driver was found
                        max_key_len = max(len(k) for k in driver)
                        for key, value in driver.items():
                            print(f"{key:<{max_key_len}} : {value}")

                elif sub_choice == "2":
                    print("""
Help Menu:
1. Searching for a driver
    - Enter the first name, surname or full name. No need to worry about capitalization.
    - Example: 'Charles', 'Leclerc', or 'Charles Leclerc' will all work.
                    """)

                elif sub_choice == "3":
                    break

                else:
                    print("\nInvalid choice. Please try again.")

        elif choice == "2":
            filter_drivers()
        elif choice == "3":
            manage_list()
        elif choice == "4":
            print("\n--- Final Interaction Log ---")
            print(get_log())
            print("\nThank you for using this program. Good Bye! :)")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
