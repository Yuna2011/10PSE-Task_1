from functions import*

def main():
    while True:
        print("F1 Menu:")
        print("1. Search Driver")
        print("2. Filter Drivers")
        print("3. Manage your list")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter driver name: ")
            max_key_len = max(len(k) for k in search_driver(name))
            for key, value in search_driver(name).items():
                print(f"{key:<{max_key_len}} : {value}")
        elif choice == "2":
            name = input("Enter driver name to add: ")
            filter_drivers()
        elif choice == "3":
            manage_list(name)
        elif choice == "4":
            print("Exiting driver list.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()