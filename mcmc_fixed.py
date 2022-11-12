# mcmc method that accepts worse proposals at a fixed probability.
def fixed(cipher_text, scoring, bigram_dictionary, acceptance_probability, Ntrials):
    key, rev_key = gen_key() # generate initial key
    letters = string.ascii_lowercase # letters for RNG to chose from

    # decrypt and initial score
    score = scoring( cipher_text, key, bigram_dictionary )
    initial_score = score
   
    score_list = [] # results
    key_list = []
    
    for i in range(Ntrials): 
        score_list.append(score) # add score and key to lists
        key_list.append(key)
        
        i = random.choice(letters) # RNG for swap
        j = random.choice(letters)

        while i == j: # make sure they're different
            i = random.choice(letters) 
            j = random.choice(letters)
    
        old_score = score # set score before swap
        key[i], key[j] = key[j], key[i] # swap entries
        new_score = scoring( cipher_text, key, bigram_dictionary ) # new score
        deltaS = new_score - old_score # change in score
        
        if deltaS > 0: # always accept better score
            score = new_score
    
        elif np.random.random() < acceptance_probability: # RNG to accept worse score
            score = new_score
    
        else: # revert back to old score
            key[i], key[j] = key[j], key[i]
            score = old_score
    
    final_phrase = decrypt(cipher_text, key)       
    return score_list, key_list, final_phrase
