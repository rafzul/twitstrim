import tweepy
from keys import *
import json
import requests


client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret, return_type=requests.Response)

expansions_items={"attachments.media_keys,geo.place_id"}
tweet_fields_items={"id,author_id,created_at,attachments,referenced_tweets,public_metrics"}
media_fields_items={"url,type"  }
place_fields_item={"country"}


public_query = client.search_recent_tweets(query="borobudur", expansions=expansions_items, tweet_fields=tweet_fields_items, media_fields=media_fields_items, place_fields=place_fields_item,max_results=10,user_auth=True,)
print(public_query.json())