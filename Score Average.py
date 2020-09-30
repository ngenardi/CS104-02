NumberOfScores = int(input("Input number of scores to be averaged: "))
Score = SumOfScores = Count = 0

while(NumberOfScores > Count):
    Score = int(input("Input a score to be averaged: "))
    Count+=1
    SumOfScores += Score
    if(NumberOfScores > Count):
        print("The average of scores so far is " + str(float(SumOfScores/Count)) + " with " + str(Count) + " of " + str(NumberOfScores) + " inputted.")

AverageOfScores = float(SumOfScores/NumberOfScores)
print("The final average of all " + str(NumberOfScores) + " scores inputted is " + str(AverageOfScores) + ".")
