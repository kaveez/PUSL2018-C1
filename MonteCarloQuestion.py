#Import random from the library
import random

def Monte_Carlo(n):
    Range_1 = 0
    Range_2 = 0
    Range_3 = 0
    Total = []
    for x in range(n):

        #Assign random values to activities 
        A = random.randint(8, 12)
        B = random.randint(10, 14)
        C = random.randint(12, 16)

        #Calculate the total days of completion
        Total_completion_days = A + B + C
        Total.append(Total_completion_days)

        #Check related range of the value 
        if Total_completion_days in range(30, 36):
            Range_1 += 1

        elif Total_completion_days in range(36, 39):
            Range_2 += 1

        elif Total_completion_days in range(39, 42):
            Range_3 += 1

    #Calculate the probability of days range 
    Range_1 = (Range_1 / n)*100
    Range_2 = (Range_2 / n)*100
    Range_3 = (Range_3 / n)*100
    return(print("\n30-35 days range={}% \n36-38 days range={}% \n39-42 days range={}% \n\nGenerated days={}".format(Range_1,Range_2,Range_3,Total)))

#User inputs
repetition_no=int(input("\nEnter the number of repetition you desired: "))
Monte_Carlo(repetition_no)