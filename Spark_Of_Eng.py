# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 09:22:06 2021

@author: tasha
"""

import pip
import tweepy
import time

consumer_key = 'QUhCAFA401cEf5UNiypN9rLjj'
consumer_secret = '2VdzUuSGsHqcaZ2ajhmDQ56fVXYKdoZcOIfp93nQiYaKimJ7C1'
access_key = '1416024492078469122-o1pBRySKUTmWYu6rFb07Ji4G9jJNQu'
access_secret = 'ahz1NRdi2M9M64YsJb41WZY1N2Tkx4rEZvq89hYcXVl5t'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

user = api.me()
search = 'engineering'
num_of_tweets = 1000


for tweet in tweepy.Cursor(api.search, search).items(num_of_tweets):
    
    try:
        
        tweet.retweet()
        print("Retweet")
        time.sleep(30)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
