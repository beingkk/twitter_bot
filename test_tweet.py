# -*- coding: utf-8 -*-
#!/karlis/local/bin/python3
"""

"""

import config
import tweepy

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

api.update_status("What up with that????")
