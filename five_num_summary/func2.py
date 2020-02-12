### START FUNCTION
def five_num_summary(items):
    # your code here
    list_conv = np.array(items)
    list_max = np.max(list_conv)
    list_median = np.median(list_conv)
    list_min = np.min(list_conv)
    list_qt1 = np.percentile(list_conv, 25)
    list_qt3 = np.percentile(list_conv, 75)
    return {'max':list_max, 'median':list_median, 'min': list_min, 'q1': list_qt1, 'q3': list_qt3}

### END FUNCTION