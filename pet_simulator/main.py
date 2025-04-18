from pet import Pet

def main():
    print("Welcome to Virtual Pet Simulator!")
    pet_name = input("What would you like to name your pet? ")
    my_pet = Pet(pet_name)
    
    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet")
        print("2. Play with your pet")
        print("3. Put your pet to sleep")
        print("4. Train your pet a new trick")
        print("5. Show learned tricks")
        print("6. Check pet's status")
        print("7. Quit")
        
        choice = input("Enter your choice (1-7): ")
        
        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.play()
        elif choice == "3":
            my_pet.sleep()
        elif choice == "4":
            trick = input("Enter the trick to teach: ")
            my_pet.train(trick)
        elif choice == "5":
            my_pet.show_tricks()
        elif choice == "6":
            my_pet.get_status()
        elif choice == "7":
            print(f"Goodbye! {my_pet.name} will miss you!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
