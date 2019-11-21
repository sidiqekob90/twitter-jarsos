import tweepy


consumer_key="ww3JhSGfv4FP2PY3HM2ql9i2B"
consumer_secret="24n6bWEmEfjHNkTobDiIrpzHfKsHWhl72PG37RkMKvDrlV3Qbe"
access_token="559525564-yn2vbf4w47TUtf4Zz6t9dRnvnlObODpEQqLe54BW"
access_token_secret="yFjmbyXm8ybQZYhmCA7qTRvKTPKgsBRzh99pLNzPPBe7t"
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
# load the twitter API via tweepy
tweepy.API(auth)

# Our search string
queryString = "pdam"

# Perform the search
matchingTweets = api.search(queryString)

print ("Searched for:", queryString)
print ("Number found:", len(matchingTweets))

# For each tweet that matches our query, print the author and text
print ("\nTweets:")
for tweet in matchingTweets:
    print (tweet.author.screen_name, tweet.author.name, tweet.text)
