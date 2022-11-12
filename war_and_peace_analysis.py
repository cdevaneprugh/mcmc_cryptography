import numpy as np
from utils_clean_text import clean_text
from utils_count_ngrams import count_bigrams, count_trigrams

# read in war and peace
data = np.load('data/wp.npz')
text = str( data['text'].item() ) # convert to string
wp = clean_text(text) # clean text

# count bigram occurrences
wp_bigram_dictionary = count_bigrams(wp)
np.save('data/wp_bigram_dictionary.npy', wp_bigram_dictionary)

# count trigrams
wp_trigram_dictionary = count_trigrams(wp)
np.save('data/wp_trigram_dictionary.npy', wp_trigram_dictionary)

# create dictionary of top n words in war and peace 
# count occurrences similar to bi/trigram dictionary

# split book at words
words = wp.split(' ')

all_words = {}
for wd in words: # add each word to dictionary
    try:
        all_words[wd] += 1
    except:
        all_words[wd] = 1

# take dictionaries we just made, sort by value, return list of n most frequent words
def get_words(dict_of_words, n):
    keys = list(dict_of_words.keys())
    vals = list(dict_of_words.values())
    
    # sort entries by number of occurrence
    zipped = zip(vals, keys)
    sort_pairs = sorted(zipped, reverse=True)

    D = {}
    for i in range(n):
        word = sort_pairs[i][1]
        D[word] = sort_pairs[i][0]
    
    return D

# get top 100 words
wp_top100_dictionary = get_words(all_words, 100)
np.save('data/wp_top100_dictionary.npy', wp_top100_dictionary)
