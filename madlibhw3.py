# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

import nltk 
from nltk.book import *
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.corpus.gutenberg.fileids()
text = input('Enter desired text: ')
print(sent_tokenize(text)) 
print(word_tokenize(text))
for i in word_tokenize(text):
    print(i)

print("START*******")




print("\n\nEND*******")
