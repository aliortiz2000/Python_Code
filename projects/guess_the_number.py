import random 
import os
import time

def guess (x):
    os.system('cls')
    
    random_number = random.randint(0,x)
    
    attempt = -1
    
    while attempt != random_number:
        attempt = int ( input (f'Guess a number between 0 and {x}: '))
        print (attempt)
        if attempt < random_number:
            print ('Too low. Try again.')
        elif attempt > random_number:
            print ('Too high. Try again.')
        else: 
            print (f'Congrats! You have guessed the number {random_number} correctly!')
            
        time.sleep(3)
        os.system('cls')  # on windows

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')
            
        
        
guess (40)