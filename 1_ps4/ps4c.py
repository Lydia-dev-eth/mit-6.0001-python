# Problem Set 4C
# Name:
# Collaborators:

import json
import ps4b # Importing your work from Part B
import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    # inFile: file
    with open(file_name, 'r') as inFile:
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist


def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.

    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"").lower()
    return word in word_list


def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("1_ps4/story.txt", "r")
    story = str(f.read())
    f.close()
    return story[:-1]


def get_story_pads():
    with open('1_ps4/pads.txt') as json_file:
        return json.load(json_file)


WORDLIST_FILENAME = 'words.txt'
### END HELPER CODE ###


def decrypt_message_try_pads(ciphertext, pads):
    '''
    Given a string ciphertext and a list of possible pads
    used to create it find the pad used to create the ciphertext

    We will consider the pad used to create it the pad which
    when used to decrypt ciphertext results in a plaintext
    with the most valid English words. In the event of ties return
    the last pad that results in the maximum number of valid English words.

    ciphertext (EncryptedMessage): The ciphertext
    pads (list of lists of ints): A list of pads which might have been used
        to encrypt the ciphertext

    Returns: (PlaintextMessage) A message with the decrypted ciphertext and the best pad
    '''
    max=0
    wordlist = load_words('1_ps4/words.txt')

    for pad in pads:
        obj_of_encryptedmessage= ps4b.EncryptedMessage(ciphertext)
        obj_of_plaintextmessage=obj_of_encryptedmessage.decrypt_message(pad)
       
        counter=0
        for word in obj_of_plaintextmessage.input_text.split():
            if is_word(wordlist,word):
                counter+=1
        if counter>= max:
            max=counter
            best_pad=pad[:]
    obj_of_encryptedmessage= ps4b.EncryptedMessage(ciphertext)
    obj_of_plaintextmessage=obj_of_encryptedmessage.decrypt_message(best_pad)
    return obj_of_plaintextmessage
    

def decode_story():
    '''
    Write yourcode here to decode Bob's story using a list of possible pads
    Hint: use the helper functions get_story_string and get_story_pads and your EncryptedMessage class.

    Returns: (string) the decoded story

    '''
    ciphertext= get_story_string() 
    one_time_pads=get_story_pads()
    decrypted_mesg= decrypt_message_try_pads(ciphertext,one_time_pads)
    return decrypted_mesg.input_text

    raise NotImplementedError  # delete this line and replace with your code here



if __name__ == '__main__':
    # # Uncomment these lines to try running decode_story()
     story = decode_story()
     print("Decoded story: ", story)
    
