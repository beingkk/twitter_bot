# -*- coding: utf-8 -*-
"""

"""

import config
import tweepy

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)





print("hey hey heyyyy")
print("Hello Git")


print("harambe")
