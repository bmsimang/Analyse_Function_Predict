import numpy as np
import pandas as pd

###


def dictionary_of_metrics(items):
    """
    Return the mean, median, variance, standard deviation,
    minimum and maximum values (descriptive statistics) of a list,
    as a dictionary, rounded to 2 decimal places.

    Args:
        items (list): list

    Return:
        dictionary: descriptive statistics, each rounded off
        to 2 decimal places

    Egs:
        dictionary_of_metrics(gauteng) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'var': 108160153.17,
                                   'std': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}
    """

    list_conv = np.array(items)
    list_mean = np.mean(list_conv)
    list_median = np.median(list_conv)
    list_var = np.var(list_conv, ddof=1)
    list_std = np.std(list_conv, ddof=1)
    list_min = np.min(list_conv)
    list_max = np.max(list_conv)
    return {'mean': round(list_mean, 2), 'median': round(list_median, 2),
            'var': round(list_var, 2), 'std': round(list_std, 2),
            'min': round(list_min, 2), 'max': round(list_max, 2)}

###


def five_num_summary(items):
    """
    Return a five number summary (the minimum value, maximum value, median,
    first quartile (q1) and third qurtile (q3)) of a list of numbers.
    Return this list as a dictionary.

    Args:
        items (list): list

    Return:
        dictionary: five number summary

    """

    list_conv = np.array(items)
    list_max = np.max(list_conv)
    list_median = np.median(list_conv)
    list_min = np.min(list_conv)
    list_qt1 = np.percentile(list_conv, 25)
    list_qt3 = np.percentile(list_conv, 75)
    return {'max': list_max, 'median': list_median, 'min': list_min,
            'q1': list_qt1, 'q3': list_qt3}

###


def date_parser(dates):
    """
    Convert the string to date-time format.

    Args:
        dates(string): string

    Return:
        list: containing strings

    """
    return [i.split()[0]for i in dates]

###


def extract_municipality_hashtags(df):
    """
    Extracts municipality name from a dataframe of tweets, removes
    hashtags and returns the modified dataframe.

    Args:
        df (dataframe): dataframe

    Return:
        dataframe containing the municipality name column and
        hashtag list column.

    """

    df["Tweets"] = [x.lower() for x in df["Tweets"]]
    df['municipality'] = df['Tweets'].map(mun_dict)
    df['hashtags'] = df['Tweets'].str.findall(r'#.*?(?=\s|$)')
    return df

###


def number_of_tweets_per_day(df):
    """
    Return a dataframe containing the dates and number of tweets per day.
    The format of date is to be yyyy-mm-dd.

    Args: df(dataframe): pandas dataframe

    Return:
        dataframe with columns containing the date and tweets

"""
    df['Date'] = [i.split()[0]for i in df["Date"]]
    df['Tweets'] = [1 for items in df['Tweets']]
    return df.groupby(['Date', ]).sum()
    pass

###


def word_splitter(df):
    """
    Return a dataframe that splits a string of tweets into
    individual words and assigns the list to a new column.

    Args: df(dataframe): pandas dataframe

    Return:
        dataframe with columns containing Tweets and Spit tweets
        as indivdual words seperated by commas.
    """

    df["Split Tweets"] = [x.lower() for x in df["Tweets"]]
    df["Split Tweets"] = [i.split() for i in df["Split Tweets"]]
    return df
    pass

###


def stop_words_remover(df):
    """
    Remove all stop words in a tokenised list from a dataframe
    containing tweets and return the modified dataframe.

    Args: df(dataframe): pandas dataframe

    Return:
        dataframe with columns containing Tweets (original tweets)
        and Without Stop Words (tweets with the stop words removed).

    """

    mastr = []
    df['Without Stop Words'] = df['Tweets']
    for columnData in df['Tweets']:
        a = columnData.lower()
        k = a.split()
        for key, value in stop_words_dict.items():
            if key == 'stopwords':
                for i in value:
                    if i in k:
                        k.remove(i)
                    else:
                        continue
            mastr.append(k)
    if len(df['Without Stop Words']) == len(df['Tweets']):
        for v in range(len(df['Tweets'])):
            df['Without Stop Words'][v] = mastr[v]
    return df
