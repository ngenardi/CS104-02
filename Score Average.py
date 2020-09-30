NumberOfScores = int(input("Input number of scores to be averaged: "))
Rounding = int(input("Insert the number of decimal places the average score is to be rounded to: "))
Score = SumOfScores = Count = 0

while(NumberOfScores > Count):
    Score = int(input("Input a score to be averaged: "))
    Count+=1
    SumOfScores += Score
    if(NumberOfScores > Count):
        print("The average of scores so far is " + str(round(float(SumOfScores/Count),Rounding)) + " with " + str(Count) + " of " + str(NumberOfScores) + " inputted.")

AverageOfScores = round(float(SumOfScores/NumberOfScores), Rounding)
print("The final average of all " + str(NumberOfScores) + " scores inputted is " + str(AverageOfScores) + ".")
