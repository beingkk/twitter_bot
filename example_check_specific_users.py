from twitter_classes import *

# Example script for checking specific users
filename = "example.dat"

client = TwitterClient()
client.set_tweet_storage(filename)

# Check Elon Musk and Donal Trump
client.set_user_list(['44196397','25073877'])
tweets = client.get_tweets_from_user_list(num_tweets=5)

client.store_tweets(tweets, order='normal')
