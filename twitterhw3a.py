# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy
from textblob import TextBlob
import sys

# Boilerplate code here
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)


def main():                                         # write code within one function that can run later
  cfg = {                                           # Unique code from Twitter
    "consumer_key"        : "cKKu7YX8zB4MxdIaorIFAIUrB",
    "consumer_secret"     : "EfhAxqvWP7VoFVTxPO4GJDlKgjiqYLiLSSCxtOaDSwBHS7WFQa",
    "access_token"        : "2546126607-MwJvheq6bGtvvJk3XsZju5XNYFWABrsvgKMBv9z",
    "access_token_secret" : "ugAOGH8F9C7f8hFIGjHXA3lC1KeuA9kwI7WNQavf7GIgr" 
    }

  api = get_api(cfg)                                # set variable equal to function get_api(cfg) that connects to Twitter account
  image_path = "media/corgi.jpg"                    # direct the image file using a relative path of the image
  tweet = "#UMSI206 #Proj3"
  media = api.update_with_media(image_path, tweet)  # sends image and tweet to Twitter account
  

if __name__ == "__main__":
  main()

#print("""No output necessary although you 
	#can print out a success/failure message if you want to.""")