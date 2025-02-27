# Kyle Stowe
# 2/13/2025
# P1HW2
# a program that calculates the price of a trip

##Pseudocode
##3. Ask user to enter their budget
##4. Ask user to enter travel destination
##5. Ask user for amount they will spend on gas
##6. Ask user for amount they will spend on accommodation
##7. Ask user for amount they will spend on food
##8. Add expenses
##9. Subtract expenses from budget
##10. Display results

#input
print("This program will calculate your travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
location = str(input("Enter your travel destination: "))
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
hotel = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("How much do you need for food? "))
print("\n")

#calc
amount = budget - (gas + hotel + food)

#output
print("-"*12,"Travel Expenses","-"*12)
print("Location:           ",location)
print("Initial Budget:     $"+str(budget))
print("Fuel:               $"+str(gas))
print("Accomodation:       $"+str(hotel))
print("Food:               $"+str(food))
print("-"*41)
print()
print(f"Remaining Balance:  ${amount:.2f}")
