NumberOfScores = int(input("Input number of scores to be averaged: "))
Score = SumOfScores = Count = 0

while(NumberOfScores > Count):
    Score = int(input("Input a score to be averaged: "))
    Count+=1
    SumOfScores += Score
    if(NumberOfScores > Count):
        print("The average of scores so far is " + str(round(float(SumOfScores/Count),2)) + " with " + str(Count) + " of " + str(NumberOfScores) + " inputted.")

AverageOfScores = round(float(SumOfScores/NumberOfScores), 2)
print("The final average of all " + str(NumberOfScores) + " scores inputted is " + str(AverageOfScores) + ".")
