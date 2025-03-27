# Kyle Stowe
# 3/27/25
# P4HW2
# Calculate an employee's pay and overtime pay and display these stats for every employee entered

pay = float
otPay = float
othours = int
totalpay = float
employeelist =[]
rateList = []
othoursList = []
otpayList = []
payList = []
totalPayList = []


employeeName = str(input("Enter an employee's name or Done to termintate: "))
while employeeName.lower() != "done":
    hours = int(input("How many hours did "+ employeeName +" work? "))
    rate = int(input("What is "+ employeeName +"'s pay rate? "))

    if hours <= 40:
        pay = hours * rate
        othours = 0
        otpay = 0
    else:
        pay = 40 * rate
        othours = hours - 40
        otpay = othours * (rate * 2)
    
    totalpay = pay + otpay
    employeelist.append(employeeName)
    rateList.append(rate)
    othoursList.append(othours)
    otpayList.append(otpay)
    payList.append(pay)
    totalPayList.append(totalpay)

    employeeName = (input("Enter another employee's name or Done to view results: "))

print(employeelist[0])
