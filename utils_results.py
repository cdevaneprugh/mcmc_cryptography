# compare strings
def compare_strings(decrypted_text, plain_text):
    match = 0
    for i, letter in enumerate(plain_text):
        if letter == decrypted_text[i]:
            match += 1

    results = match / len(plain_text)
    return results

# take results from mcmc, return top scores and corresponding keys
# https://www.folkstalk.com/tech/numpy-sort-array-by-another-array-with-code-examples/
def top_results(scores, keys, n):
    zipped_lists = zip(scores, keys) # zip lists
    sorted_pairs = sorted(zipped_lists, reverse=True) # sort descending order
    tuples = zip(*sorted_pairs)
    scores, keys = [list(tuple) for tuple in tuples]
    top_scores, top_keys = scores[:n], keys[:n] # return top n scores
    return top_scores, top_keys
