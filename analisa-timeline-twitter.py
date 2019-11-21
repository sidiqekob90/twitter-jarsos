# Chap02/twitter_client.py
import os
import sys
from tweepy import API
from tweepy import OAuthHandler
from tweepy import Cursor

def get_twitter_auth():
    """Setup Twitter authentication.

    Return: tweepy.OAuthHandler object
    """
    try:
        consumer_key="ww3JhSGfv4FP2PY3HM2ql9i2B"
        consumer_secret="24n6bWEmEfjHNkTobDiIrpzHfKsHWhl72PG37RkMKvDrlV3Qbe"
        access_token="559525564-yn2vbf4w47TUtf4Zz6t9dRnvnlObODpEQqLe54BW"
        access_token_secret="yFjmbyXm8ybQZYhmCA7qTRvKTPKgsBRzh99pLNzPPBe7t"
    except KeyError:
        sys.stderr.write("TWITTER_* environment variables not set\n")
        sys.exit(1)    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def get_twitter_client():
    """Setup Twitter API client.

      Return: tweepy.API object
      """
    auth = get_twitter_auth()
    client = API(auth)
    return client

if __name__ == '__main__':
	client = get_twitter_client()
 
	for status in Cursor(client.home_timeline).items(10):
		# Process a single status
		print(status.text)
