import time
import random
import tweepy
from credentials import *
import os.path

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
time_delay = 12*60*60 #12 hours delay

#api.update_status('testing a twitter bot. continue scrolling.')

def get_def():
    file = open('dir_to_lookup/barrons800.txt', 'r')
    data = file.readlines()
    while True:
        to_send = random.choice(data).strip()
        if len(to_send) < 280 and len(to_send) > 5:
            break
    return to_send

while True:
    to_write = get_def()
    print(to_write)
    api.update_status(to_write)
    time.sleep(time_delay)