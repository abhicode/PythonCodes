import sys
import tweepy
import json
from pymongo import MongoClient

consumerkey = "----"
consumersecret = "---"
accesskey = "---"
accesssecret = "---"

auth = tweepy.OAuthHandler(consumerkey,consumersecret)

auth.set_access_token(accesskey,accesssecret)
api = tweepy.API(auth)
print ('NAME' + api.me().name)

class CustomStreamListener(tweepy.StreamListener):

    connectionObject = 0
    db =0
    
    def __init__(self):
        ## Establish Mongo DB Connection
        try:
            connectionObject = MongoClient()
            self.db = connectionObject.tweetdata            
            print "hit database"
        except:
            print "Error Cant Connect"
            
    def on_status(self, status):
        print status.text
        print "ok"

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def insertData(self,data):
        data = {"Tweet":data}
        db_col = self.db.tweets
        post_id = db_col.insert(data)
        print post_id

    def on_data(self, tweet):
        print "\n"
        x = json.loads(tweet)
        print x[u'text']
        self.insertData(x[u'text'])
        ## Insert into MongoDB 

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

    
sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['Kejriwal'])
