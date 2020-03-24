## Quick Sort Implementation

def partition(array, low, high):
    '''
    This function will return the partition index.

    Arguments:
    array -- list, containing integer values in unsorted order.
    low -- int, the first index.
    high -- int, the ending index

    Return:
    i + 1 -- int, the partition index.
    '''
    i = low - 1
    partition = array[high]

    for j in range(low, high):
        if array[j] < partition:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[high], array[i+1] = array[i+1], array[high]

    return i + 1

def quick_sort(array, low, high):
    '''
    This function will perform the quick sort and sort the given array.

    Arguments:
    array -- list, containing integer values in unsorted order.
    low -- int, the starting index.
    high -- int, the ending index.

    Returns:
    array -- list, containing integer values in sorted order.
    '''
    if low < high:
        partition_index = partition(array, low, high)

        quick_sort(array, low, partition_index-1)
        quick_sort(array, partition_index+1, high)

    return array

array = [5, 2, 3, 1, 6, 4, 9 ,10, 7, 8]
print(f'Initial Array: {array}')

array = quick_sort(array, 0, len(array) - 1)
print(f'Sorted Array: {array}')
