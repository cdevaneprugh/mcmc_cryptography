import string

# counts occurrences of bigrams in input text
def count_bigrams(text):
    letters = string.ascii_lowercase + ' '

    bigram_count = {}
    for letter1 in letters: # loop through all combos
        for letter2 in letters:
            bigram = letter1 + letter2
            bigram_count[ bigram ] = 1 # initialize at 1

    # scan through text and tally occurrences
    N = len(text)-1
    for i in range( N ):
        bigram = text[i] + text[i+1] # bigram at i, i+1
        bigram_count[ bigram ] += 1 # update dictionary
    
    return bigram_count

def count_trigrams(text):
    letters = string.ascii_lowercase + ' '
    
    trigram_count = {}
    for letter1 in letters: # loop through all combos
        for letter2 in letters:
            for letter3 in letters:
                trigram = letter1 + letter2 + letter3
                trigram_count[ trigram ] = 1 # initialize at 1

    # scan through text and tally occurrences
    N = len(text)-2
    for i in range( N ):
        trigram = text[i] + text[i+1] + text[i+2] # trigram at i, i+1, i+2
        trigram_count[ trigram ] += 1 # update dictionary

    return trigram_count
