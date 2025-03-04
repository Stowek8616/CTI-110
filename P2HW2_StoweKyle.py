# Kyle Stowe
# 2/27/2025
# P2HW2
# asks for grades for each module and stores the grades with info such as average grade and sum of grades

#ask for input
module1 = float(input("Enter grade for Module 1:"))
module2 = float(input("Enter grade for Module 2:"))
module3 = float(input("Enter grade for Module 3:"))
module4 = float(input("Enter grade for Module 4:"))
module5 = float(input("Enter grade for Module 5:"))
module6 = float(input("Enter grade for Module 6:"))

#calculations
gradelist = [module1, module2, module3, module4, module5, module6]
gradesum = sum(gradelist)
gradeavg = gradesum / len(gradelist)
gradelow = min(gradelist)
gradehigh = max(gradelist)

#print results
print("-"*10,"Results","-"*10)
print(f'{"Lowest Grade :":<23}{gradelow}')
print(f'{"Highest Grade :":<23}{gradehigh}')
print(f'{"Sum of Grades:":<23}{gradesum}')
print(f'{"Average:":<23}{gradeavg:.2f}')
print("-"*29)
