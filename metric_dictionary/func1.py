### START FUNCTION
def dictionary_of_metrics(items):
    # your code here
    '''Import Numpy for this function. Convert the list into a Numpy array'''
    list_conv = np.array(items) ##Converting list to Numpy array
    list_mean = np.mean(list_conv) ##Calculating Mean
    list_median = np.median(list_conv) ####Calculating Median
    list_var = np.var(list_conv, ddof=1) ##Calculating Variance
    list_std = np.std(list_conv, ddof=1) ##Calculating Std Deviation
    list_min = np.min(list_conv) ##Calculating Min Val
    list_max = np.max(list_conv) ##Calculating Max Val
    return {'mean':round(list_mean,2), 'median':round(list_median,2), ##Converting to dictionary & rounding
            'var':round(list_var,2), 'std':round(list_std,2), 'min':round(list_min,2),
            'max':round(list_max,2)}
### END FUNCTION