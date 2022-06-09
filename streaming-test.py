import tweepy
from tweepy import StreamingClient, StreamRule
import os
from dotenv import load_dotenv
import json
import requests
import time

#load env and bearer token
load_dotenv()
bearer_token = os.getenv("bearer_token")

#define subclass of StreamingClient for custom method
class StdOutListener(StreamingClient):
    
    #define methods to return tweet
    def on_data(self,data):
        start_time = time.time()
        print(data)
        print(" -- %s seconds -- " % (time.time() - start_time))
        print("-"*50)
        

def StreamingAction():
    
    json_printer = StdOutListener(bearer_token, wait_on_rate_limit=True,return_type=dict)

    #add new rules
    rule = StreamRule(value="#JurassicWorldDominion -is:retweet -is:nullcast")
    json_printer.add_rules(rule)

    # #UTILITY: #get rules and delete rules
    # json_printer.delete_rules(["1534745760893669378","1534700026454503427"])
    # print(json_printer.get_rules())

    # #get filtered tweet
    json_printer.filter(expansions="author_id",tweet_fields="created_at")

    

StreamingAction()
