# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:53:41 2019

@author: paveli
"""

# imports
import tweepy
import config
import json

# parameters
max_tweets = 1000
begin_date = "2019-05-03"
end_date = None

filename = "cursor_data"

# keyword(keywords) for querry
# TODO: make this a list of Keywords 
keyword = "bitcoin"

# authentication
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
api = tweepy.API(auth)


print("Collecting tweets for '" + keyword + "' into file " + filename + "_" + keyword + ".dat")

# open file for the tweets
f = open(filename+"_"+keyword+".dat","w+") 

# loop over tweets and append the json
for tweet in tweepy.Cursor(api.search, tweet_mode='extended', q=keyword, lang='en', since=begin_date, until=end_date, result_type='recent').items(max_tweets):
    f.write(json.dumps(tweet._json))
    f.write('\n')
    
    
