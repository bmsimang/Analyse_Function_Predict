![Heading](https://github.com/bmsimang/Analyse_Function_Predict/blob/master/maxresdefault.jpg)

# Predict Functions Package

A package of python functions which takes in a list or a pandas dataframe and returns either a dictionary
or a list. The second set of functions takes in text data as either a list or as a dataframe and returns
a list or a pandas dataframe.

## List of Functions in the package and specifications:

<b> Dictionary_of_metrics </b> <br/>
- The function takes a list as an input.
- The function returns a dictionary('dict') with keys 'mean', 'median', 'std', 'var', 'min', and 'max' corresponding to the mean, median, standard deviation, variance, minimum and maximum respectively. Numpy functions are used for calculations.
- All numerical values are rounded to two decimal places.

<b> Five_number_summary </b> <br/>
- The function takes a list as an input.
- The function should return a dictionary('dict') with keys 'max', 'median', 'min', 'q1', and 'q3' corresponding to the maximum, median, minimum, first quartile and third quartile, respectively. Numpy functions are used for calculations.
- All numerical values are rounded to two decimal places. 
  
<b> Date_parser </b> <br/>
- The function takes a list of strings as an input.
- Each string in the input list is formatted as 'yyyy-mm-dd hh:mm:ss'.
- The function returns a list of strings where each element in the returned list contains only the date in the 'yyyy-mm-dd' format.

<b> Municipality & Hashtag Detector </b> <br/>
- The function takes a pandas dataframe as an input.
- The municipality is extracted from the tweets using the mun_dict dictonary, and the result is inserted into a new column named 'municipality' in the same dataframe.
- When a municipality is not found, the entry np.nan is used.
- A list of hashtags from tweets are extracted into a new column named 'hashtags' in the same dataframe.
- When a hashtag is not found, the entry np.nan is used.

<b> Number_of_tweets_per_day </b> <br/>
- The function takes a pandas dataframe as an input.
- The function returns a new dataframe, grouped by day, with the number of tweets for that day.
- The index of the new dataframe is named 'Date', and the column of the new dataframe is named 'Tweets', corresponding to the date and number of tweets, respectively.
- The date is formatted as yyyy-mm-dd, and is a datetime object.

<b> Word_splitter </b> <br/>
- The function takes a pandas dataframe as an input.
- The dataframe should contain a column, named 'Tweets'.
- The function splits the sentences in the 'Tweets' into a list of seperate words, and places the result into a new column named 'Split Tweets'. The resulting words are all lowercase.
- The function modifies the input dataframe directly.
- The function returns the modified dataframe.

<b> Stop_words_remover </b> <br/>
- The function takes a pandas dataframe as an input.
- The function tokenises the sentences according to the definition in function 6.
- The function removes all stop words in the tokenised list. The stopwords are defined in the stop_words_dict variable.
- The resulting tokenised list is placed in a column named "Without Stop Words".
- The function modifies the input dataframe.
- The function returns the modified dataframe.

## Prequisites
- Python 2.7 or later.
- Pip package installer.
- Bash.
- Numpy.
- Pandas.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install predict_function_package.

```bash
pip install git+https://github.com/bmsimang/Analyse_Function_Predict.git
```

If you get an error when running that command, and it contains this line somewhere in it:

```bash
pip ERR! Please try running this command again as root/Administrator.
```

You will need to run the install via sudo:

```bash
sudo pip install git+https://github.com/bmsimang/Analyse_Function_Predict.git
```
## License
This project is licensed under the MIT License.

## Authors

* [Bongani Msimanga](https://github.com/bmsimang)
* [Akshar Jadoonandan](https://github.com/AksharJ47)
* [Vinita Maharaj](https://github.com/vinita-maharaj)
* [Shraddha Rajcoomar](https://github.com/ShraddhaRajcoomar13) 
* [Azukile Kobe](https://github.com/azukilekobe) 
