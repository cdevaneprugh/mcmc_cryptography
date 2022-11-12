import numpy as np
from utils_cipher_tools import decrypt

# import war and peace dictionaries
bigram_dictionary = np.load('data/wp_bigram_dictionary.npy', allow_pickle='TRUE').item()
trigram_dictionary = np.load('data/wp_trigram_dictionary.npy', allow_pickle='TRUE').item()
top_100_words = np.load('data/wp_top100_dictionary.npy', allow_pickle='TRUE').item()

# stanford scoring
def stanford_bigram(cipher_text, key, bigram_dictionary):
    decrypted_text = decrypt(cipher_text, key) # decrypt cipher text
    words = decrypted_text.split(" ")

    score = 0 
    for i in range( len(decrypted_text)-1 ):
        bigram = decrypted_text[i] + decrypted_text[i+1] # bigram at i, i+1
        score += np.log10( bigram_dictionary[bigram] ) # update score
    
    # same process as bigrams, just uses top 100 words
    for wd in words:
        if wd in top_100_words: 
            score += np.log10( top_100_words[wd] ) # update score

    return score

def stanford_trigram(cipher_text, key, trigram_dictionary):
    decrypted_text = decrypt(cipher_text, key) # decrypt cipher text
    words = decrypted_text.split(" ")

    score = 0 
    for i in range( len(decrypted_text)-2 ):
        trigram = decrypted_text[i] + decrypted_text[i+1] + decrypted_text[i+2] # trigram at i, i+1, i+2
        score += np.log10( trigram_dictionary[trigram] ) # update score
    
    # same process as trigrams, just uses top 100 words
    for wd in words:
        if wd in top_100_words: 
            score += np.log10( top_100_words[wd] ) # update score

    return score
