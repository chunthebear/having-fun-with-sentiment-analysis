from difflib import SequenceMatcher
import pandas as pd

df = pd.read_csv('raw_data_sentiment_analysis.csv')

df_clean = df.drop_duplicates(subset=['tweets'], keep=False)

df_clean = df_clean.reset_index(drop=True)

df_clean.to_csv('cleaned_data_sentiment_analysis.csv')