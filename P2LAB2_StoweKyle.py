# Kyle Stowe
 # 2/27/2025
 # P2LAB2
 # Gives the user a cars MPG when prompted
 
# create dictionary
cars = {
    "camaro" : 18.21,
    "prius" : 52.36,
    "model s" : 110,
    "silverado" : 26
    }
# Display Results of all keys in dictionary

keys = cars.keys()
print(keys)
print()

car_input = input("Enter a vehicle to see it's mpg: ")
car_input = car_input.lower()
print()
mpg_output = cars[car_input]
#Display output
print(f"The {car_input} gets {mpg_output} mpg.\n")

distance = float(input(f"How many miles will you drive the {car_input}?"))
print()

gallons_needed = distance / mpg_output

print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_input} {distance} miles")

