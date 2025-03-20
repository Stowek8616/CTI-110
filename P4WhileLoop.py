run = "yes"
while(run.lower() == "yes"):
    print("Menu")
    print("1. Program 1")
    print("2. Program 2")
    print("3. Program 3")
    print("4. Exit the Program\n")
    choice = int(input("Please enter your choice: "))

    if choice == 1:
        print("You picked option 1!")
    elif choice == 2:
        print("You picked option 2!")
    elif choice == 3:
        print("You picked option 3!")
    elif choice == 4:
        print("You picked option 4!")
        print("Exiting the Program!")
        run = "n"
    else:
        print("Invalid input, Please choose a valid input")
        input("Press any key to continue")