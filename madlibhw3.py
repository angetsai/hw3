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
from nltk import bigrams 

print("START*******")
#nltk.corpus.gutenberg.fileids()
#text = text2 
print (text2) 
#print("\n\n")
s = " "
#print (s.join(set(text2[:150])))
print (s.join(text2[:150]))
#print(sent_tokenize(text2)) 
#print(word_tokenize(text2))
#for i in word_tokenize(text2):
    #print(i)

word = 0
for s.join(text2[:150]):     
    if word == 'NOUN':
        #replace.
        


nltk.corpus.gutenberg.fileids()
text = input('Enter desired text: ')
print(sent_tokenize(text)) 
print(word_tokenize(text))
for i in word_tokenize(text):
    print(i)        
    #text2 = word_tokenize(text2)

#wsj = nltk.corpus.treebank.tagged_words(tagset='universal')
#word_tag_fd = nltk.FreqDist(wsj)
#while s.join(text2[:150]):
 #   print([wt[0] for (wt, _) in word_tag_fd.most_common() if wt[1] == 'NOUN'])
#word_tag_pairs = nltk.bigrams(text2)
#from nltk.corpus import brown 
#brown_news_tagged = brown.tagged_words(tagset = 'universal')
#tag_fd = nltk.FreqDist(tag for (word, tag) in brown_news_tagged)
#tag_fd.most_common()
#for word in (nltk.tag.pos_tag(text2[:150])):
    #Frequency Distribution
 #   fdist2 = FreqDist(text2)
  #  print(fdist2)
   # print(fdist2.most_common(25))
        



#word_tag_pairs = nltk.bigrams(text2)
#noun_preceders = [a[1] for (a, b) in word_tag_pairs if b[1] == 'NOUN']
#fdist = nltk.FreqDist(noun_preceders)
#[tag for (tag, _) in fdist.most_common()]  
#sent = nltk.word_tokenize(text2)
#parser = nltk.ChartParser(grammar)
#nouns = parser.nbest_parse(sent)
#for noun in nouns:
    #print (noun)
#tokens = find_all_NP(noun)
#tokens1 = nltk.word_tokenize(tokens[0])
#print (tokens1)    
 
#print("Length of ",text1,"is",len(text1))
#print("Length of ",text2,"is",len(text2))

#print("Unique tokens in",text1," are: ",len(set(text1)))

#print("Unique tokens in",text2,"are: ",len(set(text2)))
#print("\n\nList of unique words")
#print(sorted(set(text2))[:15])
#print(sorted(set(text2),reverse=True)[:15])
#print("\n\nFrequency Distribution")
#Frequency Distribution
#fdist1 = FreqDist(text1)
#print(fdist1)
#print(fdist1.most_common(25))
#print("\n\nWords with more characters")
#How about "long" words
#long_words = [w for w in text1 if len(w)>15]
#print(long_words)
#print("\n\nBigrams")
#print(list(bigrams(text4))[:20]) #text8 would get me in trouble
#print("\n\nCollocations")
#print(text4.collocations())    


print("\n\nEND*******")
