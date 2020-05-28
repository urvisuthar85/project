import random
from words import word_list
import string


def get_word(word_list):
    word = random.choice(word_list)  
   # while '-' in word or ' ' in word:
    #    word = random.choice(word_list)

    return word.upper()
def display_hangman(lives):
    stages = [  # final 
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """
                ,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """
                ,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[lives]



def hangman():
    word = get_word(word_list)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6
    #print(display_hangman(lives))

    # getting user input
    while len(word_letters) > 0 and lives >= 0 :
        print(display_hangman(lives))
        
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        words_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(words_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1 
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

        if lives == 0:
            print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')
   

if __name__ == '__main__':
    hangman()
    while input("Play Again? (Y/N) ").upper() == "Y":
        #word = get_word(word_list)
        hangman()