# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the original text (150 tokens)
# 1) Print the new text

import nltk 
from nltk.book import *                                     # import all the texts from nltk book corpa          
from nltk.tokenize import sent_tokenize, word_tokenize 
import random


print("START*******")
 
print (text2)                                               # print original text of text 2

def spaced(word):                                           
	if word in [",", ".", "?", "!", ":", ";"]:
		return word
	else:
		return " " + word
        
textblank = []                                              # create empty list
text2 = text2[:150]                                         # set text 2 to only first 150 tokens of text 2

for word in text2:                                          # loop through text 2 and add all the words 
    textblank.append(spaced(word))

print ("".join(textblank))                                  # return a string that's joined together all string elements
print("\n\n")


para = "".join(textblank)                                   # use that string and set as new "text" to work with
tokens = nltk.word_tokenize(para)                           # tokenize text

tagged_tokens = nltk.pos_tag(tokens)                        # gives us a tagged list of tuples


tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","ADV":"an adverb","ADJ":"an adjective"}     # define parts of speech
substitution_probabilities = {"NN":.15,"NNS":.1,"VB":.1,"ADV":.1,"ADJ":.1}                              # set to replace nouns 15% of time and all others 10% of time

def spaced(word):
	if word in [",", ".", "?", "!", ":", ";"]:
		return word
	else:
		return " " + word

final_words = []                                                                                        # new empty list

for (word, tag) in tagged_tokens:                                                                       # loop through entire tokenized text
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:      # if tag is not one that we defined, append to list
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))                                          # or else, ask to enter a term to replace the set parts of speech
		final_words.append(spaced(new_word))

print ("".join(final_words))                                                                            


print("\n\nEND*******")
