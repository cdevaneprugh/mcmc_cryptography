# finds single letter words, tries i and a, returns best key
# removes letters form search space if enough new words appear
def single_letter_attack(cipher_text, key, bigram_dictionary, search_space):

    words = cipher_text.split(" ")
#    print('words in cipher text:',words)

    # search for single letter words
    single_letters = []
    for wd in words:
        if len(wd) == 1:
            single_letters.append(wd)
    
#    print('single letter words:', single_letters)
#    print()

    # new key for each option
    new_key_1 = key.copy()
    new_key_2 = key.copy()
   
    # for only one single letter word, do this
    if len(single_letters) == 1:
        letter = single_letters[0] # assign to variable

        # find and swap "a"
        a = [i for i in key if key[i] == "a"][0] # key for letter 'a' in original key
        new_key_1[ letter ], new_key_1[a] = new_key_1[a], new_key_1[ letter ]
#        print('swap in a')
#        decrypted_text = decrypt( cipher_text, new_key_1 )
#        print(decrypted_text)
#        print( stanford( cipher_text, new_key_1, bigram_dictionary) )
#        print( valid_words(decrypted_text) )
#        print()

        # find and swap "i"
        i = [i for i in key if key[i] == "i"][0] # key for letter 'i' in original key
        new_key_2[ letter ], new_key_2[i] = new_key_2[i], new_key_2[ letter ]
#        print('swap in i')
#        decrypted_text = decrypt( cipher_text, new_key_2 )
#        print(decrypted_text)
#        print( stanford( cipher_text, new_key_2, bigram_dictionary) )
#        print( valid_words(decrypted_text) )
#        print()
    
    # for multiple single letter words, must try both i and a
    else:    
        # first option for "a" and "i" 
        a = [i for i in key if key[i] == "a"][0] # key for value 'a' in original key
        new_key_1[ single_letters[0] ], new_key_1[a] = new_key_1[a], new_key_1[ single_letters[0] ]
        i = [i for i in key if key[i] == "i"][0] # key for value 'i' in original key
        new_key_1[ single_letters[1] ], new_key_1[i] = new_key_1[i], new_key_1[ single_letters[1] ]

        # second option for "a" and "i"
        a = [i for i in key if key[i] == "a"][0] # key for value 'a' in original key
        new_key_2[ single_letters[1] ], new_key_2[a] = new_key_2[a], new_key_2[ single_letters[1] ]
        i = [i for i in key if key[i] == "i"][0] # key for value 'i' in original key
        new_key_2[ single_letters[0] ], new_key_2[i] = new_key_2[i], new_key_2[ single_letters[0] ]

    # list of keys
    key_list = [key, new_key_1, new_key_2]
    
    # calculate scores for each key
    scores = []
    word_scores = []
    for k in key_list:
        scores.append( stanford(cipher_text, k, bigram_dictionary) )
        
        # decrypt and word score
        decrypted_text = decrypt( cipher_text, k )
        word_scores.append( valid_words(decrypted_text) )
    
#    print('scores',scores)
#    print('word scores',word_scores)

    # find best score in list of scores, return corresponding key
    best_score = max(scores)
#    print('best score', best_score)

    best_score_index = scores.index(best_score)
#    print('best index',best_score_index)
#    print()

    best_key = key_list[ best_score_index ]

    # if when using the best key, there are 2 or more valid words than the initial key
    # remove those letters from the swap space
    # initial search space
#    letters = string.ascii_lowercase
#    search_space = []
#    for i in letters:
#        search_space.append(i)
#    print('initial earch space')
#    print(search_space)
#    print()

    # list of letters in words that appeared from swapping in "a"
    decrypted_text = decrypt(cipher_text, best_key) 
    words = decrypted_text.split(' ') # split words at space
    
    new_words = []
    for wd in words:
        if wd in word_list:
            new_words.append(wd)

    print('new words',new_words)

    letters = []
    for wd in new_words:
        for ltr in wd:
            letters.append(ltr)
#    print('new word letters', letters)
    unique_letters = np.unique(letters)
#    print('unique letters', unique_letters)

    for ltr in unique_letters:
        search_space.remove(ltr)
#    print('new search space')
#    print(search_space)
#    print()
    return best_key, search_space
