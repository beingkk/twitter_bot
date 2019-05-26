#A python script to collect tweets using the tweepy API. Set the filename and keyword to run this script. It was tested that each tweet uses about 5kb (~5500 chars) of filesize. So about 200,000 tweets will use 1GB of storage. Keep that in mind.

import config
import tweepy
import json
import sys
import datetime
import os

class MyStreamListener(tweepy.StreamListener):
    def __init__(self):
        super(MyStreamListener, self).__init__()#calls the init of the parent class StreamListener
        self.tweetsFound = 0

    def on_error(self, status_code):
        if status_code == 420:
            print('ERROR 420')
            #returning False in on_error disconnects the stream
            return False
    def on_status(self, status):
        self.tweetsFound+=1

        end   = datetime.datetime.now()
        delta = end-start
        #sys.stdout.write("\r"+str(self.tweetsFound)+" tweets found; Time running: " + str(delta).split(".")[0] + "-> tweets/sec = " + str(self.tweetsFound/delta))
        sys.stdout.write("\r"+str(self.tweetsFound)+" tweets found; Time running: " + str(delta).split(".")[0] + " -> tweets/h=" + format(round(self.tweetsFound*3600/delta.seconds,2),'.2f') + ";\t~" + format(round(self.tweetsFound*5*3.6/delta.seconds,2),'.2f') + "MB/h;\tcurrent filesize=" + format(round(os.stat(filename).st_size/1000000,2),'.2f') + "MB")

        f.write(json.dumps(status._json))
        f.write("\n") # separates tweets by a new line

        #f.write("____________________\n") # add this to separate each tweet by a line

#authentication handling
auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)
api = tweepy.API(auth)

keyword="bitcoin" #keyword for the twitter stream
filename="tweets.dat" #filename where the tweets are stored

print("Collecting tweets for '" + keyword + "' into file " + filename)

f= open(filename,"w+") # open file for the tweets

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

start = datetime.datetime.now()
myStream.filter(track=[keyword])
