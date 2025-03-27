# Kyle Stowe
# 3/27/25
# P4HW1
# Collect test scores, drop the lowest score, then display the average and a letter grade

#ask for amount of grades and scores
listLength = int(input("How many scores are you entering? "))
gradelist = []
while listLength > 0:
    listLength -= 1
    score = float(input("Enter a score: "))
    while (score < 0 or score > 100):
        print("Invalid Grade")
        score = float(input("Please re-enter a score between 0-100: "))
    gradelist.append(score)

#calculations
gradelow = min(gradelist)
gradelist.remove(gradelow)
gradesum = sum(gradelist)
gradeavg = gradesum / len(gradelist)

#Find Letter Grade
if (gradeavg >= 90):
    letterGrade = "A"
elif (gradeavg >= 80):
    letterGrade = "B"
elif (gradeavg >= 70):
    letterGrade = "C"
elif (gradeavg >= 60):
    letterGrade = "D"
else:
    letterGrade = "F"

#print results
print("-"*10,"Results","-"*10)
print(f'{"Removed Score :":<23}{gradelow}')
print(f'{"Modified List:":<23}{gradelist}')
print(f'{"Score Average:":<23}{gradeavg:.2f}')
print(f'{"Final Grade:":<23}{letterGrade}')
print("-"*29)