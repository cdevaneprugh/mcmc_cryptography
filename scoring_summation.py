import numpy as np

# import bigram dictionary
bigram_dictionary = np.load('data/wp_bigram_dictionary.npy', allow_pickle='TRUE').item()

# simple summation
def summation(cipher_text, key, bigram_dictionary):
    decrypted_text = decrypt(cipher_text, key) # decrypt cipher text
        
    score = 0 
    for i in range( len(decrypted_text)-1 ):
        bigram = decrypted_text[i] + decrypted_text[i+1] # bigram at i, i+1
        score += bigram_dictionary[ bigram ] # update score
    
    return score
