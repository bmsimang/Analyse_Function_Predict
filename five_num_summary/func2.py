### START FUNCTION
def five_num_summary(items):
    '''First import Numpy. Convert the list to a Numpy array, then run numpy functions
    to find the 5 number summary'''
    # your code here
    list_conv = np.array(items)  ##Converting the list
    list_max = np.max(list_conv) ##Finding the Max
    list_median = np.median(list_conv) ##Finding the Median
    list_min = np.min(list_conv) ##Finding the Min
    list_qt1 = np.percentile(list_conv, 25) ##Finding Q1
    list_qt3 = np.percentile(list_conv, 75) ##Finding Q3
    return {'max':list_max, 'median':list_median, 'min': list_min, 'q1': list_qt1, 'q3': list_qt3} ##Returning the new dictionary

### END FUNCTION