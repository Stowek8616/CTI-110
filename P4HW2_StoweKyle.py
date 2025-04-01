# Kyle Stowe
# 3/27/25
# P4HW2
# Calculate an employee's pay and overtime pay and display these stats for every employee entered

#Declaring needed variables
employeeName = str(input("Enter an employee's name or Done to termintate: "))
employeeNum = 0
totalOtPay = 0
totalPay = 0
totalGrossPay = 0

# While loop asking for employee information
while employeeName.lower() != "done":
    hours = float(input("How many hours did "+ employeeName +" work? "))
    rate = float(input("What is "+ employeeName +"'s pay rate? "))
    print()

    # If loop calculating regular and overtime pay
    if hours <= 40:
        pay = hours * rate
        othours = 0
        otpay = 0
    else:
        pay = 40 * rate
        othours = hours - 40
        otpay = othours * (rate * 2)
    grosspay = pay + otpay
    

    # Saving numbers for multiple employees
    employeeNum += 1
    totalOtPay += otpay
    totalPay += pay
    totalGrossPay += grosspay

    # Output for employees Pay and asking if user wants to run again
    print(f'{"Hours Worked":<15}{"Pay Rate:":<12}{"OverTime":<12}{"OverTime Pay":<15}{"RegHour Pay":<15}{"Gross Pay"}')
    print("-"*100)
    print(f'{hours:<15}{rate:<12}{othours:<12}{otpay:<15}{pay:<12}{grosspay:<12}\n')
    employeeName = (input("Enter another employee's name or Done to view results: "))

# Final output for all employees
print("\nTotal number of employees entered: ", employeeNum, sep="")
print("Total amount paid for overtime: $", format (totalOtPay,'.2f'), sep="")
print("Total amount paid for regular hours: $", format (totalPay,'.2f'), sep="")
print("Total amount paid in gross: $", format (totalGrossPay,'.2f'), sep="")
