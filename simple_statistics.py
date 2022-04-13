from statistics import mean, median

def stats(my_list):
    '''
    Python project to perform some simple statistics on a list of values
    '''
    ma = max(my_list)
    mi = min(my_list)
    mn = mean(my_list)
    md = median(my_list)
    return {
        "minimum value":mi,
        "maximum_value":ma,
        "average":mn,
        "median value":md
    }
lst = [56,44,5,6,6,7,8,99,34,56,3232]
#invoke function
print(stats(lst ))