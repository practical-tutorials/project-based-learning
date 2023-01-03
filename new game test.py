import random 
import time
#--------------------------------------------------------------------------------------------------------------------------------------------------------
def main_game():
    que=1
    score=0
    u_ans=[]
    for key in questions:
        #output question no and questions
        opt_check()
        u_ans=u_ans.append(guess)
        if guess==questions.get(key):
            print('-'*25)
            print(' '*10+'--> Congratulations <-- '+' '*10)
            score=score+1
        else:
            print('-'*25)
            print(" "*4,'Good Luck Next Time','\n')
        for i in exp[que-1]:
                print("Explanation :",i)
                print('-'*25)
    return print(score)


#--------------------------------------------------------------------------------------------------------------------------------------------------------
def opt_check():
    while True:
        try:
            guess=input("Enter the Answer(True(T)/False(F):")
            guess=guess.upper()
            if guess=='T':
                guess='TRUE'
                break
            elif guess=='F':
                guess=='F'
                break
            else:
                print("Enter Correct option")
        except guess.isalpha():
            print("Enter Alphabets")
            continue
    return guess

#--------------------------------------------------------------------------------------------------------------------------------------------------------
questions={'The Big Apple is a nickname given to Washington D.C in 1971.':'FALSE',
'Copyrights depreciate over time.':'TRUE',
'People may sneeze or cough while sleeping deeply.':'FALSE',
'Electrons move faster than the speed of light.':'FALSE',
'Light travels in a straight line.':'TRUE'}
exp=[['The name refers to New York City. It originated in the 1920s when John Fitz Gerald started a horse racing column called Around the Big Apple '],
['Because copyrights have an expiration date, their value decreases as that date approaches.'],
['We can’t sneeze or cough when in deep sleep. Our body must enter a state of wakefulness to do so. '],
['Electrons are much slower than the speed of light because they have mass.'],
['Light travels in a straight line until it meets an obstacle that can influence its angle.']]
main_game()