# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

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

def get_story_string():
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        
        self.message_text = text
        self.valid_words = load_words('words.txt')

    def get_message_text(self):
        
        return self.message_text
    
    def get_valid_words(self):
        
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
       
        my_dict = {}
        for i in string.ascii_lowercase:            
             my_dict[i] = string.ascii_lowercase[(string.ascii_lowercase.index(i)+shift)%26]
        for i in string.ascii_uppercase:            
             my_dict[i] = string.ascii_uppercase[(string.ascii_uppercase.index(i)+shift)%26]
        return my_dict
    
    def apply_shift(self, shift):
        text = self.get_message_text()
        ans = ""
        my_dict = self.build_shift_dict(shift)
        for h in text:      
            index = text.index(h)
            if h in my_dict:
                ans = ans + my_dict[h]
            else:
                ans = ans + text[index]
        return ans

    
class PlaintextMessage(Message):
    def __init__(self, text, shift):
        Message.__init__(self,text)
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        return self.shift
    
    def get_encryption_dict(self):
        return self.encryption_dict.copy()
        
    def get_message_text_encrypted(self):
        return self.message_text_encrypted
    
    def change_shift(self, shift):
        self.shift = shift
        self.encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

        

class CiphertextMessage(Message):
    def __init__(self, text):
        Message.__init__(self,text)
        
    def decrypt_message(self):
        strings = list()
        my_dict = {}
        valid = self.get_valid_words()
        for i in range(0,26):
            count = 0
            strings.append(self.apply_shift(26-i))
        for i in range(0,26):   
            wordlist = strings[i].split()
            for word in wordlist:
                count = 0
                if(is_word(valid,word)):
                    count = count + 1
            my_dict[(i,strings[i])] = count
        return max(my_dict, key=my_dict.get)

if __name__ == '__main__':
    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    print()
    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (2, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    print()
    #TODO: WRITE YOUR TEST CASES HERE
    plaintext2 = PlaintextMessage('come', 4)
    print('Expected Output: gsqi')
    print('Actual Output:', plaintext2.get_message_text_encrypted())
    print()
    ciphertext = CiphertextMessage('gsqi')
    print('Expected Output:', (4, 'come'))
    print('Actual Output:', ciphertext.decrypt_message())
    print()
    #TODO: best shift value and unencrypted story 
    x = CiphertextMessage(get_story_string())
    print(x.decrypt_message())
    

    