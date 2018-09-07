import time
import random
import tweepy
from credentials import *
import os.path

def get_def():
	file = open('dir_to_lookup/barrons800.txt', 'r')
	data = file.readlines()
	while True:
		to_send = random.choice(data).strip()
		if len(to_send) < 280 and len(to_send) > 5:
			break
	return to_send

def reply():
	for status in tweepy.Cursor(api.retweets_of_me()).items():
		tweet_id = status.id_str
		parent_id = status.retweeted_status.id_str
		tweet_text = status.text
		with open("answers.txt", "a") as file:
			lines = file.readlines()

		for line in lines:
			words = line.split()
			if words[0] == parent_id and words[1].lower() == tweet_text.tolower():
				api.update_status('You are correct!',tweet_id);

def main():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	no_of_words_per_day = 6
	time_delay = (12*60*60) // no_of_words_per_day
	time_delay = 2
	word_count = 0;
	todays_words = []


	while True:
		if word_count < no_of_words_per_day:
			to_write = get_def()
			tweet = api.update_status(to_write)
			tweet_id = tweet.id_str
			word = (tweet_id, to_write.split(':')[0].strip())
			todays_words.append(word)
			word_count += 1

			reply()
			time.sleep(time_delay)

		elif word_count == no_of_words_per_day:
			print('\ntodays_words:',todays_words)
			question = list(random.choice(todays_words))
			print('random word:', question[1])

			with open("answers.txt", "a") as file:
				file.write(str(question).strip('[').strip(']')+"\n")

			todays_words.clear()
			word_count = 0;
			print("Going to sleep.....")
			time.sleep(12*60*60)

if __name__ == '__main__':
	main()