import numpy as np
import pandas as pd


###
def dictionary_of_metrics(items):
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
    return [i.split()[0]for i in dates]

###
def extract_municipality_hashtags(df):

    mun_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}

    df["Tweets"] = [x.lower() for x in df["Tweets"]]
    df['municipality'] = df['Tweets'].map(mun_dict)
    df['hashtags'] = df['Tweets'].str.findall(r'#.*?(?=\s|$)')
    return df

### 
def number_of_tweets_per_day(df):
    df['Date'] = [i.split()[0]for i in df["Date"]]
    df['Tweets'] = [1 for items in df['Tweets']]
    return df.groupby(['Date', ]).sum()
    pass

###
def word_splitter(df):
    df["Split Tweets"] = [x.lower() for x in df["Tweets"]]
    df["Split Tweets"] = [i.split() for i in df["Split Tweets"]]
    return df
    pass

###
def stop_words_remover(df):
    df["Without Stop Words"] = [x.lower() for x in df["Tweets"]]
    df["Without Stop Words"] = [i.split() for i in df["Without Stop Words"]]
    return df
    pass 