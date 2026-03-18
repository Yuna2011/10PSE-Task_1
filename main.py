from functions import*

def main():
    while True:
        print("\F1 Menu:")
        print("1. Search Driver")
        print("2. Add Driver to List")
        print("3. View Driver List")
        print("4. Remove Driver")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter driver name: ")
            print(f"Search for {name}'s details") #Replace with function later
        elif choice == "2":
            name = input("Enter driver name to add: ")
            print(f"Add {name} to driver list") #Replace with function later
        elif choice == "3":
            print('View driver list') #Replace with function later
        elif choice == "4":
            name = input("Enter driver name to remove: ")
            print(f'Remove {name} from driver list') #Replace with function later
        elif choice == "5":
            print("Exiting driver list.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()