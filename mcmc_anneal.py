# mcmc with annealing
def anneal(cipher_text, scoring, bigram_dictionary):
    
    Tmax = 10
    Tmin = 1.e-3
    tau = 1.e4

    t = 0
    T = Tmax
    
    key, rev_key = gen_key() # generate initial key
    
    # letters for RNG to chose from
    search_space = []
    for i in string.ascii_lowercase:
        search_space.append(i)

    # decrypt and initial score
    score = scoring( cipher_text, key, bigram_dictionary )
    initial_score = score

    score_list = [] # results
    key_list = []
    
    while T > Tmin:
        t +=1 # advance time 
        T = Tmax * np.exp(-t/tau) # update T

        score_list.append(score) # add score and key to lists
        key_list.append(key)
        
        i = random.choice(search_space) # RNG for swap
        j = random.choice(search_space)

        while i == j: # make sure they're different
            i = random.choice(search_space) 
            j = random.choice(search_space)
    
        old_score = score # set score before swap
        key[i], key[j] = key[j], key[i] # swap entries
        new_score = scoring( cipher_text, key, bigram_dictionary )
        deltaS = new_score - old_score # change in score
        
        if deltaS > 0: # always accept better score
            score = new_score
    
        elif np.random.random() < np.exp(deltaS/T): # RNG to accept worse score. exp decreases as T decreases
            score = new_score
    
        else: # revert back to old score
            key[i], key[j] = key[j], key[i]
            score = old_score
        
        if t == 30000:
            key, search_space = single_letter_attack( cipher_text, key, bigram_dictionary, search_space)

    final_phrase = decrypt(cipher_text, key)
    return score_list, key_list, final_phrase
