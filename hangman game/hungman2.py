import random
from words import word_list
import string

def get_word(word_list):
   word = random.choice(word_list)
   return word.upper()


def hungman():
   word = get_word(word_list)
   word_letter = set(word)
   alphabet = set(string.ascii_uppercase)
   used_letter = set()

   lives = 6

   while len(word_letter)>0 and lives>= 0:
      print('you have',lives,'lives left and you have used these letters: '," ".join(used_letter))

      print(display_hangman(lives))
      words_list = [letter if letter in used_letter else '-' for letter in word]
      print('Current word: ', ' '.join(words_list))

      user_letter = input('guess the letter------->>>').upper()
      if user_letter in alphabet - used_letter:
         used_letter.add(user_letter)
         if user_letter in word_letter:
            word_letter.remove(user_letter)
            print('')
         else:
            lives = lives - 1
            print('\nYour letter,', user_letter, 'is not in the word.')
      elif user_letter in used_letter:
         print("\nYour letter,', user_letter, 'is not in the word.")
      elif lives == 0:
         print('You died, sorry. The word was', word)
      else :
         print('\nThat is not a valid letter.')
   else :
      print('YAY! You guessed the word', word, '!!!!!!!')




   




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



if __name__ == "__main__":
   hungman()
   while input('Play Again? (Y/N)' ).upper() == "Y":
      hungman()


