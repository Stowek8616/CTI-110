keepGoing = "yes"
while keepGoing.lower() =="yes":
    num = int(input("Enter an integer: "))
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