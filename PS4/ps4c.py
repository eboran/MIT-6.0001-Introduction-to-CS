# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list
### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        
        self.message_text = text
        self.valid_words = load_words('words.txt')
        
    def get_message_text(self):
       
        return self.message_text
        
    def get_valid_words(self):
   
        return self.valid_words[:]        
                
    def build_transpose_dict(self, vowels_permutation):
        my_dict={}
        vowels_permutation_upper = vowels_permutation.upper()
        for i in range(5):
            my_dict[VOWELS_LOWER[i]] = vowels_permutation[i]
            my_dict[VOWELS_UPPER[i]] = vowels_permutation_upper[i]
        for i in range(21):
            my_dict[CONSONANTS_LOWER[i]] = CONSONANTS_LOWER[i]
            my_dict[CONSONANTS_UPPER[i]] = CONSONANTS_UPPER[i]
        return my_dict
    
    def apply_transpose(self, transpose_dict):

        text = self.get_message_text()
        new = str()
        for i in text:
            if i in transpose_dict:
                new += transpose_dict[i]
            else:
                new += i
        return new
                
            
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
 
        SubMessage.__init__(self, text)
        
        
    def decrypt_message(self):
        listofvowels = get_permutations(VOWELS_LOWER)
        listofdict = list()
        valid = self.get_valid_words()
        for i in listofvowels:
            listofdict.append(self.build_transpose_dict(i))
        transposedlist = list()
        for i in listofdict:
            transposedlist.append(self.apply_transpose(i))
        my_dict = {}
        for s in transposedlist:
            wordlist = s.split()
            count = 0
            for word in wordlist:
                if(is_word(valid,word)):
                    count += 1
                my_dict[s] = count
        return max(my_dict, key=my_dict.get)     
            
    

if __name__ == '__main__':

    # Example test case
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    print()
    #TODO: WRITE YOUR TEST CASES HERE
    message2 = SubMessage("adept deuce cower")
    permutation2 = "ouiea"
    enc_dict2 = message2.build_transpose_dict(permutation)
    print("Original message:", message2.get_message_text(), "Permutation:", permutation2)
    print("Expected encryption:", "odupt duacu cewur")
    print("Actual encryption:", message2.apply_transpose(enc_dict2))
    enc_message2 = EncryptedSubMessage(message2.apply_transpose(enc_dict2))
    print("Decrypted message:", enc_message2.decrypt_message())
