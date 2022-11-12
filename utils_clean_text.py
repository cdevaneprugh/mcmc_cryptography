import re

# clean input text of everything but lowercase and spaces
def clean_text(text):
    text = text.lower()
    text = re.sub('- ', '', text) # remove "- " (line continuations)
    text = re.sub('[^a-z ]+', '', text) # remove everything but letters and spaces
    text = re.sub(' +', ' ', text) # replace multiple spaces with single
    return text
