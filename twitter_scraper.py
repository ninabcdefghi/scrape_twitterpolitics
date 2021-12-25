import snscrape.modules.twitter as sntwitter
import csv
import pandas as pd

def scrape_users(users, zeitraum):
    for user in users:

        tweets_list = []
        
        conditions = 'from:{} {}'.format(user, zeitraum)

        for i,tweet in enumerate(sntwitter.TwitterSearchScraper(conditions).get_items()): #declare a username 
            tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.user.username]) #declare the attributes to be returned
        
        tweets_df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

        # add to csv
        tweets_df.to_csv('my_csv.csv', mode='a', header=False)

def main():
	
	users = ["OlafScholz", "jensspahn", "c_lindner", "SWagenknecht", ]
	zeitraum = "since:2017-10-24 until:2021-10-27"
	
	scrape_users(users, zeitraum)

main()