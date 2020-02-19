![Heading](https://github.com/bmsimang/Analyse_Function_Predict/blob/master/maxresdefault.jpg)

# Predict Functions Package

A package of python functions which take in a list or a pandas dataframe and returns either a dictionary
or a list. The second set of functions take in text data as either a list or as a dataframe and returns
a list or or pandas dataframe

## List of Functions in the package and specifications:

<b> Dictionary_of_metrics </b> <br/>
- The function should take a list as input.
- The function should return a `dict` with keys `'max'`, `'median'`, `'min'`, `'q1'`, and `'q3'` corresponding to the maximum, median, minimum, first quartile and third quartile, respectively. You may use numpy functions to aid in your calculations.
- All numerical values should be rounded to two decimal places.

<b> Five_num_summary </b> <br/>
- The function should take a list as input.
- The function should return a `dict` with keys `'max'`, `'median'`, `'min'`, `'q1'`, and `'q3'` corresponding to the maximum, median, minimum, first quartile and third quartile, respectively. You may use numpy functions to aid in your calculations.
- All numerical values should be rounded to two decimal places. 
  
<b> Date_parser </b> <br/>
- The function should take a list of strings as input.
- Each string in the input list is formatted as 'yyyy-mm-dd hh:mm:ss'.
- The function should return a list of strings where each element in the returned list contains only the date in the 'yyyy-mm-dd' format.

<b> Municipality & Hashtag Detector </b> <br/>
- Function should take a pandas dataframe as input.
- Extract the municipality from a tweet using the mun_dict dictonary given below, and insert the result into a new column named 'municipality' in the same dataframe.
- Use the entry np.nan when a municipality is not found.
- Extract a list of hashtags from a tweet into a new column named 'hashtags' in the same dataframe.
- Use the entry np.nan when no hashtags are found.

<b> Number_of_tweets_per_day </b> <br/>
- It should take a pandas dataframe as input.
- It should return a new dataframe, grouped by day, with the number of tweets for that day.
- The index of the new dataframe should be named Date, and the column of the new dataframe should be 'Tweets', corresponding to the date and number of tweets, respectively.
- The date should be formated as yyyy-mm-dd, and should be a datetime object. Hint: look up pd.to_datetime to see how to do this.

<b> Word_splitter </b> <br/>
- It should take a pandas dataframe as an input.
- The dataframe should contain a column, named 'Tweets'.
- The function should split the sentences in the 'Tweets' into a list of seperate words, and place the result into a new column named 'Split Tweets'. The resulting words must all be lowercase!
- The function should modify the input dataframe directly.
- The function should return the modified dataframe.

<b> Stop_words_remover </b> <br/>
- It should take a pandas dataframe as input.
- Should tokenise the sentences according to the definition in function 6. Note that function 6 cannot be called within this function.
- Should remove all stop words in the tokenised list. The stopwords are defined in the stop_words_dict variable defined at the top of this notebook.
- The resulting tokenised list should be placed in a column named "Without Stop Words".
- The function should modify the input dataframe.
- The function should return the modified dataframe.

## Prequisites
- Python 2.7 or later
- Pip package installer
- Bash

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install predict_function_package.

```bash
pip install  https://github.com/bmsimang/Analyse_Function_Predict.git
```

If you get an error when running that command, and it contains this line somewhere in it:

```bash
pip ERR! Please try running this command again as root/Administrator.
```

You will need to run the install via sudo:

```bash
sudo pip install  https://github.com/bmsimang/Analyse_Function_Predict.git
```



