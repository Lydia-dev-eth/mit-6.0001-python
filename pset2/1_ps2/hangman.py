# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()
 
def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    # to check if all the words are guessed
    
    letters_guessed = [l.lower() for l in letters_guessed]
    for  char in  secret_word:
        
        if char not in letters_guessed:# to check if each words are in the secret word
            return False
            
    return True      

          
    

    


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    #FILL IN YOUR CODE HERE AND DELETE "pass"
    list_word= ["*"]*len(secret_word)# first we creat a list with astroid and then replace it with words that are guessed correctley
    letters_guessed = [l.lower() for l in letters_guessed]
    for count,char in enumerate( secret_word):
        
        if char in  letters_guessed:
            list_word[count]= char
    return "".join(list_word)  
    
       
        
    
    


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    all_letters=string.ascii_lowercase
    not_guessed_letters=[]
     
    
    if len(letters_guessed)==0:
        return all_letters
    for char in all_letters:
        if char not in letters_guessed:
            not_guessed_letters+=[char]
    
    return "".join(not_guessed_letters) 


def choose_letter(secret_word, get_available_letter):# a function that reveals random letter from secret word
    unique_letter="" #intiate the unique strin that is got from both parameters 
    for char in secret_word:
        if char in get_available_letter:
            unique_letter=char
    new= random.randint(0, len( unique_letter)-1)
    revealed_letter= unique_letter[new]
    return revealed_letter
        

    



def hangman(secret_word, with_help):
 """
 secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------  
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
 """
 # FILL IN YOUR CODE HERE AND DELETE "pass"
 no_guesses=10
 letters_guessed=[]
 word_progress = get_word_progress(secret_word, letters_guessed)
 print("Welcome to Hangman!")
 length= len(secret_word)
 print(f"I am thinking of a word that is {length} letters long.")
 print("-------------")
 while no_guesses>0:
  if word_progress== secret_word:
     break
  available_letters = get_available_letters(letters_guessed)
  print(f"you have {no_guesses} guesses left.")
  print(f"Available letters: {available_letters}")
  user_input= input("Please guess a letter: ").lower()
  if word_progress== secret_word:
     break
# for help 
  if with_help and user_input == "!" and no_guesses >= 3:
    revealed_letter = choose_letter(secret_word, available_letters)
    letters_guessed += [revealed_letter]
    word_progress = get_word_progress(secret_word, letters_guessed)  # recalc after adding hint
    print(f"letter revealed: {revealed_letter}")
    print(word_progress)
    no_guesses -= 3
    print("-------------")
    continue
  elif with_help and user_input == "!":
    print(f"Oops! Not enough guesses left: {word_progress}")
    print("-------------")
    continue

#  Already guessed letter
  if user_input in letters_guessed:
    print(f"Oops! You've already guessed that letter: {word_progress}")
    print("-------------")
    continue

#  Invalid input
  lowercase_letters = string.ascii_lowercase
  if len(user_input) != 1 or user_input not in lowercase_letters:
    print(f" Oops! That is not a valid letter. Please input a letter from the alphabet: {word_progress}")
    print("-------------")
    continue

#  Correct guess
  if user_input in secret_word:
    letters_guessed += [user_input]
    word_progress = get_word_progress(secret_word, letters_guessed)  # recalc after adding letter
    print(f"Good guess: {word_progress}")
    print("-------------")
    continue

#  Incorrect vowel guess
  elif user_input in "aeiou":
    letters_guessed += [user_input]
    word_progress = get_word_progress(secret_word, letters_guessed)  # recalc after adding letter
    no_guesses -= 2
    print(f"Oops! That letter is not in my word: {word_progress}")
    print("-------------")

# Incorrect consonant guess
  else:
    letters_guessed += [user_input]
    word_progress = get_word_progress(secret_word, letters_guessed)  # recalc after adding letter
    no_guesses -= 1
    print(f"Oops! That letter is not in my word: {word_progress}")
    print("-------------")
 result=has_player_won(secret_word, letters_guessed)
 uniqeu_letter=list (set(secret_word)) 
 uniqeu_letter= "".join(uniqeu_letter)
 total_score = (no_guesses +4*len(uniqeu_letter)) + (3* len( secret_word))
 if result:
    print("Congratulations, you won!")
    print(f"Your total score for this game is: {total_score}")

 else:
    print(print(f"Sorry, you ran out of guesses. The word was {secret_word}."))  
 
 print()
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

     secret_word = choose_word(wordlist)
     with_help = False
     hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    

