import random
import os

def rock_paper_scissors ():
    os.system('cls')
    user = input ("Choose 'r' for rock, 'p' for paper or 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])
    
    if user == computer:
        return "It's a tie"
    else:
        if  is_win(user, computer):
            return f"\nYou won\nYou: {user}     Computer: {computer}"
        else:
            return f"\nComputer won\nYou: {user}     Computer: {computer}"
        
        
    # r > s, s > p, p > r      
def is_win (player, opponent):
    # Return true if player wins
    if (player == 'r' and opponent == 's') \
        or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True
    else:
        return False
    
    
print (rock_paper_scissors())