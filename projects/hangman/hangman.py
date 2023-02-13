import random
import string
import os
from words import words
from hangman_visual import lives_visual_dict as visual

# Randomly chooses something from the list and validates 
def get_valid_word (words):
    word = random.choice(words).upper()
    while '-' in word or ' ' in word :
        word = random.choice(words).upper()
        
    return word

def hangman ():
    os.system('cls')  # on windows
    word = get_valid_word(words)
    word_letters = set(word) # Letter in the word
    
    alphabet = set (string.ascii_uppercase) 
    used_letters = set() # The letters you have tried
    
    lives = 7
    
    while lives != 0 and len (word_letters) != 0 :
    
        # Getting user input 
        user_letter  = input ("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters :
            used_letters.add(user_letter)
            if user_letter in word_letters : 
                word_letters.remove(user_letter)
                for spaces_letters in word :
                    if spaces_letters in used_letters :
                        print (f" {spaces_letters} " , end='')
                    else :
                        print (" _ " , end='')
                print ("\n")
            else :
                lives -= 1 # Takes away a life when wrong
                print (visual[lives])
                print (f"\nYour letter, '{user_letter}', is not in the word.")
        elif user_letter in used_letters :
            print ("\nYou have already used that letter.")
        else : 
            print ("\nThat it's not a valid letter")
            
    if lives == 0 :
        print (visual[lives])
        print ('You died, sorry. The word was', word)
    elif len (word_letters) == 0 :
        print ('YAY! You guessed the word', word, '!!')
        
    
    
if __name__ == '__main__':
    hangman()    