#Unicompiler Internship Task 1
#NUMBER GUESSING:
#Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range.
#Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue,and his score gets reduced.
#The clue can be multiples, divisible, greater or smaller, or a combination of all.




import random as r
import math
print("**************************WELCOME TO THE NUMBER GUESSING GAME****************************")
print("********Some Instructions and Rules********")
print("-----------------You will be given 5 chances to guess the correct number----------------")
print("--------For correct guess you will earn 1 point and lose for wrong guess---------")
print("--------------MAXIMUM CHANCE:5 -------MINIMUM CHANCE:0---------------")
print("-----------------Press enter to play the game-------------------")


print("fix the range from where to where the number must be randomly chosen.")
lower_bound = int(input("Enter the lower bound of the range : "))
upper_bound = int(input("Enter the upper bound of the range : "))
generated_number = r.randint(lower_bound,upper_bound)
chance=5
i=1
while i<=5:
    guessed=int(input("Enter the number between "+ str(lower_bound)+" and "+ str(upper_bound)+": "))
    i=i+1
    if guessed==generated_number :
              print("****Congratulations,you have won!!!****")
              print("Your Guess is Correct and You have taken attempts for the right answer.")
              break
    elif(guessed>generated_number ):
              print("Guessed number is greater than generated number")
              chance=chance-1
              print("Your chances left:"+str(chance))
              print("Sorry,Try another chance!")

    elif(guessed<generated_number ):
              print("Guessed number is lesser than generated number")
              chance= chance-1
              print("Your chances left:"+str(chance))
              print("Sorry,Try another chance!")

    elif(guessed%5==0):
              print("Divisible by 5")
              chance = chance-1
              print("Your chances left:"+str(chance))
              print("Sorry,Try another chance!")
if(chance==0) :
    print("Your chances hace been exhausted.")
    print("OOPS!!!YOU LOSE THE GAME")
