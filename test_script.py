# -*- coding: utf-8 -*-
#!/karlis/local/bin/python3
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
<<<<<<< HEAD


print("harambe")
=======
print("Another one")
>>>>>>> 6a5bf5ca2da0cc79a97502ba35aa904e692af6e6
