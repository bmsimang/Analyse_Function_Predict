def number_of_tweets_per_day(df):
    df['Date'] = [i.split()[0]for i in df["Date"]]
    df['Tweets'] = [1 for one in df['Tweets']]
    df = df.groupby('Date').sum()
    return df
    pass
