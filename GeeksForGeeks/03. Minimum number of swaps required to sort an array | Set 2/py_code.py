## Minimum number of swaps required to sort an array | Set 2

def count_min_swaps(array):
    '''
    This function will count the minimum number of swaps to sort an array.

    Argument:
    array -- list, containing integer values.

    Returns:
    count -- int, minimum number of swaps.
    '''
    length = len(array)
    count = 0
    
    for i in range(length):
        pos = i

        for j in range(i+1, length):
            if array[pos] > array[j]:
                pos = j
        if pos != i:
            array[pos], array[i] = array[i], array[pos]
            count += 1
    
    return count

array = [3, 5, 2, 4, 6, 8]
print(count_min_swaps(array))
