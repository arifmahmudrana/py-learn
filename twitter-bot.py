import tweepy
import time

auth = tweepy.OAuthHandler('', '')
auth.set_access_token('', '')
api = tweepy.API(auth)

user = api.me()
print(user.name)  # prints your name.
print(user.screen_name)
print(user.followers_count)

search = "arifmahmudrana"
numberOfTweets = 2


def limit_handle(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(1000)


for follower in limit_handle(tweepy.Cursor(api.followers).items()):
    if follower.name == 'arifmahmudrana':
        print(follower.name)
        # follower.follow()


for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
    try:
        tweet.favorite()
        print('Retweeted the tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
