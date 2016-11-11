# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy
from textblob import TextBlob
import sys
import os
import requests

# Boilerplate code here
def get_api(cfg):
  auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
  auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
  return tweepy.API(auth)
  
#def tweet_image(url, message):
#    api = get_api(cfg)
#    filename = 'temp.jpg'
#    request = requests.get(url, stream=True)
#    if request.status_code == 200:
#        with open(filename, 'wb') as image:
#            for chunk in request:
#                image.write(chunk)

#        api.update_with_media(filename, status=message)
#        os.remove(filename)
#    else:
#        print("Unable to download image")


def main():
  # Unique code from Twitter
  cfg = { 
    "consumer_key"        : "cKKu7YX8zB4MxdIaorIFAIUrB",
    "consumer_secret"     : "EfhAxqvWP7VoFVTxPO4GJDlKgjiqYLiLSSCxtOaDSwBHS7WFQa",
    "access_token"        : "2546126607-MwJvheq6bGtvvJk3XsZju5XNYFWABrsvgKMBv9z",
    "access_token_secret" : "ugAOGH8F9C7f8hFIGjHXA3lC1KeuA9kwI7WNQavf7GIgr" 
    }

  api = get_api(cfg)
  image_path = "media/corgi.jpg" 
  tweet = "#UMSI206 #Proj3"
  #status = api.update_status(status=tweet) 
  media = api.update_with_media(image_path, status=tweet)
  #twitter.update_status(status='hello this is a status', media_ids=image_ids['media_id'])
  #url = "https://img.buzzfeed.com/buzzfeed-static/static/2014-10/20/13/enhanced/webdr05/enhanced-5564-1413824442-8.jpg"
  #tweet = "#UMSI206 #Proj3"
  #status = api.update_status(status=tweet,url)
  #tweet_image(url, message) 
  #status = api.update_with_media(image_path, tweet)
  # Yes, tweet is called 'status' rather confusing
  

if __name__ == "__main__":
  main()

#print("""No output necessary although you 
	#can print out a success/failure message if you want to.""")