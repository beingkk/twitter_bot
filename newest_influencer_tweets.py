from twitter_classes import *

""" Checks the newest tweets with respect to the last saved tweet """

filename = "influencer_tweets.dat"
last_saved_tweet_id_filename = "influencer_tweets_last.dat"
last_saved_tweet_id = open(last_saved_tweet_id_filename).read()

client = TwitterClient()
client.set_tweet_storage(filename)
tweets = client.get_own_timeline(minID = last_saved_tweet_id)

if tweets:
    all_tweets = []
    for tweet in tweets:
        all_tweets.append(tweet)

    # Save the newest tweet's id
    newest_tweet = tweets[0]._json["id"]
    open(last_saved_tweet_id_filename,"w+").write(str(newest_tweet))

    # Check if there are any tweets between the newest batch and the old ones
    while tweets:
        oldest_new_tweet = tweets[-1]._json["id"]
        tweets = client.get_own_timeline(minID = last_saved_tweet_id, maxID = oldest_new_tweet-1)
        for tweet in tweets:
            all_tweets.append(tweet)

    # Store the new tweets
    client.store_tweets(all_tweets)
    tweet_count = len(all_tweets)
    print("{} new tweets!".format(tweet_count))
else:
    print("No new tweets. Try again later.")
