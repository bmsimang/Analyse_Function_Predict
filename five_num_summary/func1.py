### START FUNCTION
def dictionary_of_metrics(items):
    # your code here
    list_conv = np.array(items)
    list_mean = np.mean(list_conv)
    list_median = np.median(list_conv)
    list_var = np.var(list_conv, ddof=1)
    list_std = np.std(list_conv, ddof=1)
    list_min = np.min(list_conv)
    list_max = np.max(list_conv)
    return {'mean':round(list_mean,2), 'median':round(list_median,2),
            'var':round(list_var,2), 'std':round(list_std,2), 'min':round(list_min,2),
            'max':round(list_max,2)}
### END FUNCTION