## Selection Sort Implementation

def sel_sort(array):
    '''
    This function performs selection sort on a given array.

    Argument:
    array -- list, containing integer values.

    Returns:
    array -- list, sorted in ascending order.
    '''
    length = len(array)

    for i in range(length):
        pos = i
        for j in range(i+1, length):
            if array[pos] > array[j]:
                pos = j
        array[i], array[pos] = array[pos], array[i]
    
    return array

array = [5, 4, 3, 1, 2]
print(sel_sort(array))
