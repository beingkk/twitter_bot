import config
import tweepy
import csv
import json

#### TWITTER AUTHENTICATER
class TwitterAuthenticator():

    def authenticate_twitter_app(self):
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.access_token, config.access_token_secret)
        return auth

#### TWITTER STREAMER
class TwitterStreamer():
    """ Here we define which tweets and from which users to stream """
    def __init__(self):
        self.twitter_autenticator = TwitterAuthenticator()

    def stream_tweets(self, stored_tweets_file, user_list=None):
        # This handles Twitter authetification and the connection to Twitter Streaming API
        listener = TwitterListener(stored_tweets_file)
        auth = self.twitter_autenticator.authenticate_twitter_app()
        stream = Stream(auth, listener)

        # This line filter Twitter Streams to capture data by the keywords:
        stream.filter(track=hash_tag_list)

#### TWITTER STREAM LISTENER
class TwitterListener(tweepy.StreamListener):
    """ Here we define what to do with the streamed tweets """
    def __init__(self, tweets_file):
        self.saved_tweets_filename = tweets_filename

    def on_data(self, data):
        try:
            print(data)
            with open(self.saved_tweets_filename, 'a') as file:
                file.write(data)
            return True
        except BaseException as e:
            print("Error on_data %s" % str(e))
        return True

    def on_error(self, status_code):
        if status_code == 420:
            # Returning False on_data method in case rate limit occurs.
            print('ERROR 420')
            return False
        print(status)

#### TWITTER CLIENT
class TwitterClient():
    """ Here we define other interactions with twitter that aren't streams """
    def __init__(self):
        self.auth = TwitterAuthenticator().authenticate_twitter_app()
        self.twitter_client = tweepy.API(self.auth)
        self.user_list = None
        self.tweet_storage_filename = None

    def get_twitter_client_api(self):
        return self.twitter_client

    # Define the file in which to store tweets from this client instance
    def set_tweet_storage(self, tweet_storage_filename):
        self.tweet_storage_filename = tweet_storage_filename

    # Try to get the maximum number of tweets from your own timeline
    def get_own_timeline(self, minID = None, maxID = None, count = 200):
        return self.twitter_client.home_timeline(count=count, since_id=minID, max_id=maxID)

    # Methods below allow to get tweets from a given set of users
    def set_user_list(self,user_list):
        self.user_list = user_list

    def set_user_list_from_file(self, user_list_file):
        self.user_list = list()
        with open(user_list_file,'r') as csv_file:
            users = csv.reader(csv_file, delimiter=',')
            for row in users:
                id = row[1].strip()
                self.user_list.append(id)
            self.user_list.pop(0)

    def get_tweets_from_user_list(self, num_tweets):
        # Limited to 1500 requests per 15 minutes, but I haven't tested the limits yet
        tweets = []
        for user in self.user_list:
            for tweet in tweepy.Cursor(self.twitter_client.user_timeline, id=user).items(num_tweets):
                tweets.append(tweet)
        return tweets

    def store_tweets(self, tweets, order='reverse'):
        
        with open(self.tweet_storage_filename, 'a') as file:
            if order == 'normal':
                for tweet in tweets:
                    file.write(json.dumps(tweet._json))
                    file.write('\n')
            elif order == 'reverse':
                num_tweets = len(tweets)
                for j in range(num_tweets-1,-1,-1):
                    file.write(json.dumps(tweets[j]._json))
                    file.write('\n')
            file.close()

#### Laurens's tweet reading function
def get_tweets_from_file(filename):
    data = []
    with open(filename) as f:
        for line in f:
            data.append(json.loads(line))
    return data
