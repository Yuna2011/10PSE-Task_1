from functions import*

def main():
    while True:
        print("\nF1 Menu:")
        print("1. Search Driver")
        print("2. Filter Drivers")
        print("3. Manage your list")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter driver name: ")
            driver = search_driver(name)
            if driver:  # driver was found
                max_key_len = max(len(k) for k in driver)
                for key, value in driver.items():
                    print(f"{key:<{max_key_len}} : {value}")
        elif choice == "2":
            filter_drivers()
        elif choice == "3":
            manage_list()
        elif choice == "4":
            print("Exiting driver list.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()