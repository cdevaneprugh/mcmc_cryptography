import string
import random

# scramble input characters and create keys
def gen_key(letters=string.ascii_lowercase):
    random_letters = random.sample(letters, len(letters)) # shuffle letters
    
    encryption_key = dict( zip(letters, random_letters) )
    key = dict( zip(random_letters, letters) )
    encryption_key[' '], key[' '] = ' ', ' ' # add spaces
    
    return key, encryption_key

# encrypt
def encrypt(phrase, encryption_key) :
    jumbled_phrase = ""
    
    for i in range( len(phrase) ) :
        jumbled_phrase += encryption_key[phrase[i]]
    
    return jumbled_phrase

# decrypt
def decrypt(jumbled_phrase, key):
    decrypted_phrase = ""

    for i in range( len(jumbled_phrase) ):
        decrypted_phrase += key[jumbled_phrase[i]]

    return decrypted_phrase
