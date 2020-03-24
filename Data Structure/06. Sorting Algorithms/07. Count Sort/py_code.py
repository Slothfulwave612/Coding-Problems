## Count Sort Implementation

def count_sort(array):
    '''
    This function will perform count sort to sort the given array.

    Argument:
    array -- list, containing integer values in unsorted order.

    Returns:
    sorted_array -- list, containing integer values in sorted order.
    '''
    length = len(array)
    count_num = [0] * (length + 1)
    sum_num = []
    sorted_array = [0] * length

    for num in array:
        count_num[num] += 1
    
    summed = 0
    for num in count_num:
        summed += num
        sum_num.append(summed)
    
    for i in range(length):
        sorted_array[sum_num[array[i]] - 1] = array[i]
        sum_num[array[i]] -= 1
    
    return sorted_array

array = [5, 2, 4, 3, 1, 2, 5, 4, 2, 1, 2]
print(count_sort(array))
