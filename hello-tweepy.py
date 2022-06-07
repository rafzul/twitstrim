import tweepy
from keys import *
import json
import requests


client = tweepy.Client(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token=access_token, access_token_secret=access_token_secret)

# # query = "news"    
# # tweets = api.search_recent_tweets(query=query, max_results=10)
# public_tweets = api.get_home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)
# handler = tweepy.OAuth1UserHandler(
#    consumer_key, consumer_secret
# )
expansions_items={"attachments.media_keys,referenced_tweets.id"}
tweet_fields_items={"id,author_id,created_at"}
media_fields_items={"url,type"}


public_tweets = client.get_home_timeline(expansions=expansions_items, tweet_fields=tweet_fields_items, media_fields=media_fields_items, max_results=5)
# author_id, expansions=expansions_items, tweet_fields=tweet_fields_items, 
print(public_tweets)
# for tweet in public_tweets.data:
#     print()

# print(handler.get_authorization_url())

# verifier = input("Input Pin: ")
# access_token, access_token_secret = handler.get_access_token(verifier)

# print(f"Access_token is {access_token}")
# print(f"Access_token_secret is {access_token_secret}")
