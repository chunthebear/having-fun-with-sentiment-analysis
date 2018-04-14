import pandas as pd

#read raw data from csv file
df = pd.read_csv('raw_data_sentiment_analysis.csv')

#remove tweets that are the same
df_clean = df.drop_duplicates(subset=['tweets'], keep=False)

#re-assign index
df_clean = df_clean.reset_index(drop=True)

#write the cleaned data into a new csv file
df_clean.to_csv('cleaned_data_sentiment_analysis.csv')

#to do: write an algorithm to remove tweets that are similiar but are not 100% the same 