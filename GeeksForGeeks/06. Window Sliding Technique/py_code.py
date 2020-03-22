## maximum sum of ‘k’ consecutive elements in the array
## Window Sliding Technique

import sys

def max_sum(array, k):
    '''
    This function will give max sum for k consecutive numbers in an array.

    Arguments:
    array -- list, containing integer values.
    k -- int, number of consecutive elements.

    Returns:
    sum_max -- int, maximum sum of k consecutive elements.
    '''
    length = len(array)
    sum_max = - sys.maxsize

    for i in range(length - k + 1):
        count_sum = 0
        for j in range(k):
            count_sum += array[i+j]
        sum_max = max(sum_max, count_sum)
    
    return sum_max

array = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum(array, k))
