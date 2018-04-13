import tweepy
import csv
import pandas as pd
from tweepy.auth import OAuthHandler
from textblob import TextBlob


apiKey = "INSERT-KEY"
apiSecret = "INSERT-SECRET"

accessToken = "INSERT-TOKEN"
accessTokenSecret = "INSERT-TOKEN-SECRET"

auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessTokenSecret)

api = tweepy.API(auth, wait_on_rate_limit=True)

csvFile = open('raw_data_sentiment_analysis.csv', 'a', newline='')

csvWriter = csv.writer(csvFile)

csvWriter.writerow(["tweets", "polarity", "subjectivity"])

for tweet in tweepy.Cursor(api.search, q="Mark Zuckerberg AND Congress" ,count=100, lang="en", since="2018-04-10").items():
    text = TextBlob(tweet.text)
    csvWriter.writerow([tweet.text.encode('utf-8'), text.sentiment.polarity, text.sentiment.subjectivity])

