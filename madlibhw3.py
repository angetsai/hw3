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
import random


print("START*******")
 
print (text2) 

def spaced(word):
	if word in [",", ".", "?", "!", ":", ";"]:
		return word
	else:
		return " " + word
        
textblank = []
text2 = text2[:150]
for word in text2:
    textblank.append(spaced(word))

print ("".join(textblank)) 
print("\n\n")


para = "".join(textblank) 
tokens = nltk.word_tokenize(para)

tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples


tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","ADV":"an adverb","ADJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"ADV":.1,"ADJ":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":", ";"]:
		return word
	else:
		return " " + word

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))

print ("".join(final_words))


print("\n\nEND*******")
