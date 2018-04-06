# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
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
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        for n in letters_guessed:
            if i==n:
                secret_word = secret_word.replace(i,"")
    if secret_word == "":
        return True
    else:
        return False



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if not i in letters_guessed:
            secret_word = secret_word.replace(i,"_ ")
    return secret_word




def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    all = string.ascii_lowercase
    for i in letters_guessed:
        if i in string.ascii_lowercase:
            all = all.replace(i,"")
    return all
    
num_guess = 6
num_warnings = 3
letters_guessed = list()
count = 0
def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is", len(secret_word), " letters long.")
    print("You have 3 warnings left.")
    print("-------------")
    print("You have 6 guesses left.")
    print("Available letters: abcdefghijklmnopqrstuvwxyz")
    def myfunc(secret_word):
        global count
        global num_guess
        global num_warnings
        global letters_guessed
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("Congratulations, you won!")
            score = count * num_guess
            print("Your total score for this game is: ",score)
        else:
            guess = str(input("Please guess a letter: "))
            if guess in letters_guessed:
                num_warnings = num_warnings - 1
                print("You have", num_guess, "guesses left.")
                print("Available Letters: ", get_available_letters(letters_guessed))
                print("Oops! You've already guessed that letter. You have", num_warnings ,"warnings left: ")
                print(get_guessed_word(secret_word, letters_guessed))
                if num_warnings < 1:
                    print("Sorry, you ran out of warnings.")
                    print("You have lost")
                else:
                    return myfunc(secret_word)
            elif guess not in secret_word:
                if guess in ["a","e","i","o"]:
                    num_guess = num_guess - 2
                else:
                    num_guess = num_guess - 1
                if num_guess < 1:
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                    print("-----------")
                    print("Sorry, you ran out of guesses. The word was else.")
                else:
                    letters_guessed.extend([guess])
                    print("You have", num_guess, "guesses left.")
                    print("Available Letters: ", get_available_letters(letters_guessed))
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                    print("-----------")
                    return myfunc(secret_word)
            else:
                letters_guessed.extend([guess])
                print("You have", num_guess, "guesses left.")
                print("Available Letters: ", get_available_letters(letters_guessed))
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                print("-----------")
                count = count + 1
                return myfunc(secret_word)
    return myfunc(secret_word)
   


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if len(my_word) == 0:
        return True
    else:
        return (my_word[0] == other_word[0] or my_word[0] == "_") and match_with_gaps(my_word[1:len(my_word)],other_word[1:len(other_word)])                

                
            
            


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in my_word:  #boşlukları kapatır
        if i == " ":
            my_word = my_word.replace(i,"")
    new_wordlist = list()
    for i in range(0,len(wordlist)):
        if len(wordlist[i]) == len(my_word):
            new_wordlist.append(wordlist[i])
    result_list=list()
    for other_word in new_wordlist:
        if match_with_gaps(my_word, other_word) == True:
            result_list.append(other_word)
    return result_list
                

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    def myfunc(secret_word):
        global count
        global num_guess
        global num_warnings
        global letters_guessed
        if is_word_guessed(secret_word, letters_guessed) == True:
            print("Congratulations, you won!")
            score = count * num_guess
            print("Your total score for this game is: ",score)
        else:
            guess = str(input("Please guess a letter: "))
            if guess in letters_guessed:
                num_warnings = num_warnings - 1
                print("You have", num_guess, "guesses left.")
                print("Available Letters: ", get_available_letters(letters_guessed))
                print("Oops! You've already guessed that letter. You have", num_warnings ,"warnings left: ")
                print(get_guessed_word(secret_word, letters_guessed))
                if num_warnings < 1:
                    print("Sorry, you ran out of warnings.")
                    print("You have lost")
                else:
                    return myfunc(secret_word)
            elif guess not in secret_word:
                if guess != "*":
                    if guess in ["a","e","i","o"]:
                        num_guess = num_guess - 2
                    else:
                        num_guess = num_guess - 1
                if num_guess < 1:
                    print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                    print("-----------")
                    print("Sorry, you ran out of guesses. The word was else.")
                else:
                    if guess == "*":
                        print(show_possible_matches(get_guessed_word(secret_word, letters_guessed)))
                        return myfunc(secret_word)
                    else:
                        letters_guessed.extend([guess])
                        print("You have", num_guess, "guesses left.")
                        print("Available Letters: ", get_available_letters(letters_guessed))
                        print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))
                        print("-----------")
                        return myfunc(secret_word)
            else:
                letters_guessed.extend([guess])
                print("You have", num_guess, "guesses left.")
                print("Available Letters: ", get_available_letters(letters_guessed))
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
                print("-----------")
                count = count + 1
                return myfunc(secret_word)
    return myfunc(secret_word)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
#    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
