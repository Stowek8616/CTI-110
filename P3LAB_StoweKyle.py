# Kyle Stowe
# 3/6/25
# P3LAB_StoweKyle
# Program that allows you to enter money and see how many dollars, dimes, and pennies would make up that amount

money = float(input("Enter the amount of money as a float: "))
change = int(money * 100)

if change == 0:
    print("No change")

dollars = int(change // 100)
remainder = int(change % 100)
quarters = int(remainder // 25)
remainder = (remainder % 25)
dimes = int(remainder // 10)
remainder = (remainder % 10)
nickels = int(remainder // 5)
remainder = (remainder % 5)
pennies = int(remainder)

if dollars >= 1: 
    print(dollars, end=' ')
    if dollars ==1:
        print("Dollar")
    else:
        print("Dollars")

if quarters >= 1:  
    print(quarters, end=' ')
    if quarters ==1:
        print("Quarter")
    else:
        print("Quarters")

if dimes >= 1:  
    print(dimes, end=' ')
    if dimes ==1:
        print("Dime")
    else:
        print("Dimes")

if nickels >= 1:  
    print(nickels, end=' ')
    if nickels ==1:
        print("Nickel")
    else:
        print("Nickels")

if pennies >= 1: 
    print(pennies, end=' ')
    if pennies ==1:
        print("Penny")
    else:
        print("Pennies")
