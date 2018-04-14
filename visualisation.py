import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read cleaned data from csv file
df = pd.read_csv('cleaned_data_sentiment_analysis.csv')

#count number of tweets which are positve or negative or neutral
numPositive = df.polarity[df.polarity > 0.1].count()
numNegative = df.polarity[df.polarity < -0.1].count()
numNeutral = df.polarity[df.polarity <= 0.1].count() - numNegative

#make it a pie chart to visualise the percentage
toPlot = pd.Series([numPositive/len(df), numNegative/len(df), numNeutral/len(df)])
toPlot.plot.pie(figsize=(6, 6), labels=["Positive", "Negative", "Neutral"], title = "Sentiment Analysis")
plt.show()