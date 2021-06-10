import tweepy
from tweepy import AppAuthHandler

consumer_key: str =  ''
consumer_secret: str = ''
#bearer_token: str = ''

auth = AppAuthHandler(consumer_key, consumer_secret)

api = tweepy.API(auth)

for status in tweepy.Cursor(api.home_timeline).items(10):
    # Process a single status
    print(status.text)