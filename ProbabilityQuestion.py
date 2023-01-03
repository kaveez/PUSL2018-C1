#Import random from the library
import random

def simulate():
    #Generate a list of three random integers representing three children, 0 denotes as a boy and 1 denotes as a girl
    gender_expectation = [random.randint(0,1)for _ in range(3)]

    #Check 'the at least one child is a girl and all are girls' expectation
    at_least_one_girl = 1 in gender_expectation 
    all_girls = gender_expectation == [1,1,1]
    return at_least_one_girl and all_girls


#Count the expections of at least one child is a girl and all three are girls
number_of_successes = 0
#Run the simlation for 1000 times
number_of_runs = 1000
for _ in range(number_of_runs):
        if simulate():
            number_of_successes += 1

#Probability calculation
probability = number_of_successes / number_of_runs
#Print the result of probability 
print(f'Probability of at least one of the children is a girl, all are gilrs : {probability}')

