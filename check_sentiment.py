import config
import tweepy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

class MyStreamListener(tweepy.StreamListener):
    def on_error(self, status_code):
        if status_code == 420:
            print('ERROR 420')
            #returning False in on_error disconnects the stream
            return False
    def on_status(self, status):
        if status.truncated:
            print(status.extended_tweet['full_text'])
            print(analyser.polarity_scores(status.text))
        else:
            print(status.text)
            print(analyser.polarity_scores(status.text))

        print("--------------------------------------")

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['trump'],follow=["2211149702"])
