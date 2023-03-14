# cryptography via mcmc methods

The general idea is to break a cipher text with mcmc methods. I analyze a reference text (in this case War and Peace) by counting the occurences of sequential 2 and 3 letter n-grams in the text. These counts are stored in a dictionary which is then used to score the cipher text as decryption keys are tried out. The idea is that the decryption key will improve as the score improves, ideally getting us all the way to a fully decrypted cipher text. See the write up for more details.
