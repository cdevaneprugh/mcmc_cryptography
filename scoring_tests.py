import numpy as np
import string
from utils_cipher_tools import decrypt
from scoring_stanford import stanford_bigram, stanford_trigram
from single_letter_attack import single_letter_attack


# import war and peace dictionaries
bigram_dictionary = np.load('data/wp_bigram_dictionary.npy', allow_pickle='TRUE').item()
trigram_dictionary = np.load('data/wp_trigram_dictionary.npy', allow_pickle='TRUE').item()
top_100_words = np.load('data/wp_top100_dictionary.npy', allow_pickle='TRUE').item()
unix_dictionary = np.load('data/unix_dictionary.npy', allow_pickle='TRUE').item()

###################################################################
#
# KEYS FOR TESTING
#
###################################################################

key1 = {'l': 'a', 'n': 'b', 'g': 'c', 'y': 'd', 's': 'e', 'e': 'f', 'a': 'g', 'v': 'h', 'x': 'i', 'i': 'j', 'p': 'k', 'm': 'l', 'z': 'm', 'h': 'n', 'k': 'o', 't': 'p', 'r': 'q', 'c': 'r', 'u': 's', 'o': 't', 'b': 'u', 'f': 'v', 'd': 'w', 'j': 'x', 'w': 'y', 'q': 'z', ' ': ' '}
key2 = {'l': 'a', 'n': 'b', 'g': 'y', 'y': 'd', 's': 'e', 'e': 'f', 'a': 'g', 'v': 'h', 'x': 'i', 'i': 'm', 'p': 'w', 'm': 'l', 'z': 'j', 'h': 'n', 'k': 'o', 't': 'p', 'r': 'q', 'c': 'r', 'u': 's', 'o': 't', 'b': 'u', 'f': 'v', 'd': 'k', 'j': 'x', 'w': 'c', 'q': 'z', ' ': ' '}
key3 = {'l': 'v', 'n': 'n', 'g': 'y', 'y': 'd', 's': 'e', 'e': 'f', 'a': 'g', 'v': 'h', 'x': 'i', 'i': 'm', 'p': 'w', 'm': 'u', 'z': 'j', 'h': 'b', 'k': 'o', 't': 'p', 'r': 'q', 'c': 'r', 'u': 's', 'o': 't', 'b': 'l', 'f': 'a', 'd': 'k', 'j': 'x', 'w': 'c', 'q': 'z', ' ': ' '}
key4 = {'l': 'v', 'n': 'n', 'g': 'y', 'y': 'a', 's': 'e', 'e': 'f', 'a': 'g', 'v': 'h', 'x': 'u', 'i': 'm', 'p': 'o', 'm': 'i', 'z': 'j', 'h': 'b', 'k': 't', 't': 'p', 'r': 'q', 'c': 'r', 'u': 's', 'o': 'w', 'b': 'l', 'f': 'd', 'd': 'k', 'j': 'x', 'w': 'c', 'q': 'z', ' ': ' '}
key5 = {'l': 'v', 'n': 'n', 'g': 'y', 'y': 'a', 's': 'g', 'e': 'f', 'a': 'e', 'v': 'h', 'x': 'x', 'i': 'm', 'p': 'o', 'm': 'i', 'z': 'j', 'h': 'b', 'k': 't', 't': 'q', 'r': 'p', 'c': 'r', 'u': 's', 'o': 'w', 'b': 'l', 'f': 'd', 'd': 'k', 'j': 'u', 'w': 'c', 'q': 'z', ' ': ' '}
key6 = {'l': 'r', 'n': 'n', 'g': 'f', 'y': 'a', 's': 'g', 'e': 'y', 'a': 'e', 'v': 'm', 'x': 't', 'i': 'h', 'p': 'o', 'm': 'i', 'z': 'j', 'h': 'b', 'k': 'x', 't': 'q', 'r': 'p', 'c': 'v', 'u': 's', 'o': 'w', 'b': 'l', 'f': 'd', 'd': 'k', 'j': 'u', 'w': 'c', 'q': 'z', ' ': ' '}

keys = [key1, key2, key3, key4, key5, key6]

###################################################################
#
# TEST KEYS
#
###################################################################

# phrase
cipher_text = 'zywd ynf zmbb oanx jr xia imbb xp gaxwi y rymb pg oyxal'

for k in keys:
    d = decrypt(cipher_text, k) 
    print(d)

    print( stanford_bigram(cipher_text, k, bigram_dictionary) )
    print( stanford_trigram(cipher_text, k, trigram_dictionary) )
    print()
