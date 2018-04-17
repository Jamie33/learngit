url = 'https://mobile.twitter.com/NausGlobal/status/974481846070231040'



import tweepy
from tweepy import OAuthHandler

consumer_key = 'kDMX2rApBKm1D2kCy0NfeW4Ru'
consumer_secret = 'wrnmQvH90gB0Req3Q5lnm6ruNercTyFjeLHlb6sETfeCPKZX4N'
access_token = '3272682498-PcewubomkAKDoDyxQVhk5wCdKWqIaN8ykjOAaUI'
access_secret = 'F3unOH8LobxrhZOHL36DMOydwHtKDQs4ZFcvRN0SimfwN'


auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth,proxy='127.0.0.1:1087')
public_tweets = api.user_timeline('NausGlobal')
for tweet in public_tweets:
    print(tweet.text)