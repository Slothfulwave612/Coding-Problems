## the maximum sum of ‘k’ consecutive elements in the array.

import sys

def max_sum(array, k):
    '''
    This function will calculate the maximum sum for k consecutive elements.

    Arguments:
    array -- list, containing integer values.
    k -- int, k consecutive integers.

    Returns:
    sum_max -- int, maximum sum of k consecutive elements.
    '''
    length = len(array)
    sum_max = - sys.maxsize

    window_sum = sum([array[index] for index in range(k)])

    for i in range(length-k):
        window_sum = window_sum - array[i] + array[i+k]
        sum_max = max(sum_max, window_sum)
    
    return sum_max

array = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4

print(max_sum(array, k))
