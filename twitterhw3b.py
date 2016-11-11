# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

## Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob
import sys
import json

def uprint(*objects, sep=' ', end='\n', file=sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep=sep, end=end, file=file)
    else:
        f = lambda obj: str(obj).encode(enc, errors='backslashreplace').decode(enc)
        print(*map(f, objects), sep=sep, end=end, file=file)


# Unique code from Twitter
access_token = "2546126607-MwJvheq6bGtvvJk3XsZju5XNYFWABrsvgKMBv9z"
access_token_secret = "ugAOGH8F9C7f8hFIGjHXA3lC1KeuA9kwI7WNQavf7GIgr"
consumer_key = "cKKu7YX8zB4MxdIaorIFAIUrB"
consumer_secret = "EfhAxqvWP7VoFVTxPO4GJDlKgjiqYLiLSSCxtOaDSwBHS7WFQa"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users


public_tweets = api.search('Corgis')

subjectivity = []
polarity = []

for tweet in public_tweets:
    uprint(tweet.text)
    analysis = TextBlob(tweet.text)
    polarity.append(analysis.sentiment[0])
    subjectivity.append(analysis.sentiment[1])

avg_sub = sum(subjectivity)/len(subjectivity)
avg_pol = sum(polarity)/len(subjectivity) 


for tweet in public_tweets:
	uprint(tweet.text)

#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#Sentiment Analysis - Understand and Extracting Feelings from Data
 
print("Average subjectivity is", avg_sub)
print("Average polarity is", avg_pol)


