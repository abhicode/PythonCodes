import sys
import tweepy
import json

consumerkey = "....."
consumersecret = "....."
accesskey = "......"
accesssecret = "......"

auth = tweepy.OAuthHandler(consumerkey,consumersecret)

auth.set_access_token(accesskey,accesssecret)
api = tweepy.API(auth)
print ('NAME WHO IS ACCESSING THIS' + api.me().name)


class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print status.text
        print "ok"

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_data(self, tweet):
        print "\n"
        x = json.loads(tweet)
        print x[u'text']

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['Pepsi'])
