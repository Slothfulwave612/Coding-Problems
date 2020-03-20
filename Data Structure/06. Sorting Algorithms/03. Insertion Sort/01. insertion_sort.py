## Insertion Sort Implementation

def insertion_sort(array):
    '''
    This function performs insertion sort on a given array.

    Argument:
    array -- list, containing the list of intergers.

    Returns:
    array -- list, sorted in ascending order.
    '''
    length = len(array) 

    for i in range(1, length):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    
    return array

array = [5, 4, 3, 2, 1]
print(insertion_sort(array))
