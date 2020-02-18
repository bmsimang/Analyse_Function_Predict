### function which splits the sentences in a dataframe's column into a list of the separate words.
def word_splitter(df):
    df["Split Tweets"] = [x.lower() for x in df["Tweets"]]
    df["Split Tweets"] = [i.split() for i in df["Split Tweets"]]
    return df