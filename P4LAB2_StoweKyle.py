keepGoing = "yes"
while keepGoing.lower() =="yes":
    num = int(input("Enter an integer 12 or less: "))
    while num < 0 or num > 12:
        print("Invalid Entry!")
        print("Input must be a positive number that is 12 or less")
        num = int(input("Enter an integer 12 or less: "))
    print()
    if(num >= 0):
        for i in range(1,12+1):
            print(f'{num} * {i} = {num*i}')
    else:
        print("ERROR: Cannot enter negative value")
    print()
    keepGoing = input("Do you want to run the program again? Enter yes or no. ")
print()
print("Exiting the program...")
