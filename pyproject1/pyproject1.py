#!usr/bin/env python3
# rock paper scissors 
# Conditionals
import random

def my_game():
    

    my_score = 0
    your_score = 0
    our_choices = ('rock', 'paper' , 'scissors')

    print(f'let us play a game of {our_choices}')
    print(f'you go first')
    
    #number of game rounds = 3
    counter = 0
    your_answer = " "
    my_answer = " "
    
   
    #while round of game is less than 3
    while counter < 3:
        #collecting your choice  
        print(f'make your choice')
        your_answer = input('your choice --->').strip().lower()

        #check for invalid input
        #list comprehension: for each x in choices, set x to true if x == your_answer else set x to false
        check = [True if x == your_answer else False for x in our_choices]

        #any() function returns true if any item in the iterable is true otherwise, it returns false

        #if check is not true, print else ignore if statement
        if not any(check):
            print(f'your choice is invalid! please choose between {our_choices}')

            #continue() The continue returns the control to the beginning of the while loop
            continue

        my_answer = random.choice(our_choices)
        
        print(f'your choice is : {your_answer} and my choice is : {my_answer}')
        counter += 1
        
        #logic to check winner according to rules of rock, paper, scissors

        if your_answer == my_answer:
            my_score += 0.5
            your_score += 0.5
            print('is a tie, we have each earned 0.5 points')

        if your_answer == 'rock' and my_answer == 'paper':
            print('paper covers rock, i win 1 point.')
            my_score += 1

        elif your_answer == 'paper' and my_answer == 'rock':
            print('paper covers rock, you win 1 point')
            your_score += 1

        if your_answer == 'rock' and my_answer == 'scissors':
            print('rock crushes scissors, you win 1 point')
            your_score += 1                 

        elif your_answer == 'scissors' and my_answer == 'rock':
            print('rock crushes scissors, i win 1 point')                     
            my_score += 1    
        
        if your_answer == 'paper' and my_answer == 'scissors':
            print('scissors slices paper, i win 1 point')
            my_score += 1

        elif your_answer == 'scissors' and my_answer == 'paper':
            print('scissors slices paper, you win 1 point')
            your_score +=1

    else:
        if my_score > your_score:
            print(f'Game Over!!! i won this round at {my_score} points')

        elif my_score < your_score:
            print(f'Game Over!!! you won this round at {your_score} points')

        else:
            print(f'Game Over!!! this round is a tie')


my_game()

        

