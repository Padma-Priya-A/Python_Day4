#Get input for score out of 100.If score is < 35="Poor Student".if score is greater than 35 but < than 70 ="Average Student" if score is greater than 70="Good Student"

Score=int(input("Enter the score out of 100:"))
if(Score<35):
    print("POOR STUDENT")
elif(35<Score<70):
    print("AVERAGE STUDENT")
else:
    print("GOOD STUDENT")
