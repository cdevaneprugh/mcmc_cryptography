import numpy as np
import matplotlib.pyplot as plt
from mcmc_anneal import anneal
from mcmc_fixed import fixed
from scoring_stanford import stanford_bigram, stanford_trigram
from utils_cipher_tools import gen_key, encrypt, decrypt
from utils_results import compare_strings, top_results

# import war and peace dictionaries
bigram_dictionary = np.load('data/wp_bigram_dictionary.npy', allow_pickle='TRUE').item()
trigram_dictionary = np.load('data/wp_trigram_dictionary.npy', allow_pickle='TRUE').item()
top_100_words = np.load('data/wp_top100_dictionary.npy', allow_pickle='TRUE').item()
unix_dictionary = np.load('data/unix_dictionary.npy', allow_pickle='TRUE').item()

###################################################################
#
# PLAIN TEXT 
#
###################################################################

# full rhyme 
rhyme = "jack and jill went up the hill to fetch a pail of water jack fell down and broke his crown and jill came tumbling after"

# phrase from project handout
phrase = "jack and jill went up the hill to fetch a pail of water"

###################################################################
#
# START EXPERIMENT
#
###################################################################

plain_text = phrase
scoring_method = stanford_bigram

key, encryption_key = gen_key()
cipher_text = encrypt(plain_text, encryption_key)
scores, keys, final_text = annealing(cipher_text, scoring_method, wp_c)
print(final_text)

plt.figure()
plt.plot(scores)
plt.title('Score Convergence')
plt.xlabel('Step Number')
plt.ylabel('Score')
plt.show()

#accuracy = []
#successful_runs = 0 # for fully decrypted phrase
#counter = 0
#for i in range(100):
#    counter += 1
#
#    # encrypt plain text
#    key, encryption_key = gen_key()
#    cipher_text = encrypt(plain_text, encryption_key)
#    
#    # run mcmc
#    scores, keys, final_phrase = annealing(cipher_text, scoring_method, wp_c)
#    
#    # calculate results
#    A = compare_str(final_phrase, plain_text)
#    accuracy.append(A)
#
#    if A == 1.0:
#        successful_runs += 1
#
#    if counter % 10 == 0:
#        print(f'experiment: {counter}')
#
#mean_accuracy = np.mean(accuracy)
#print('accuracy:', mean_accuracy)
#print('good runs:', successful_runs)
