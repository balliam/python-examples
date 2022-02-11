import tweepy


#auth info
auth = tweepy.OAuthHandler("slqn2PzfFvb7ME7Do7Gq0saHU", "YH4j5wr0WdjSk5ozKm20ezr7knbABIH3Xl3mgPrCZdnabhYUef")
auth.set_access_token("1491946659114278917-z1rDNNxGBxvtWSP3i7NDxUd3qINNRl",
                      "vXVcK0hPMEzypdV9w7Rn7n4IIcHZPhp5188vHZcaZD7Tn")
api = tweepy.API(auth)

#try to auth
try:
    api.verify_credentials()
    print("Authentication Successful")
except:
    print("Authentication Error")


#garbo
user_hashtag = input('Type your hashtag: ')
date = input('Enter timeframe to search hashtag word in YYYY-MM-DD: ')

test = api.search_tweets(q=user_hashtag, count=100, until=date)

for tweet in test:
    print(tweet.text)