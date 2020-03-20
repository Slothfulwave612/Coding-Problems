## Bubble Sort Implementation

def bubble_sort(array):
    '''
    The function performs bubble sort on a given array.

    Argument:
    array -- list, containing integer values.

    Returns:
    array -- list, sorted in ascending order.
    '''
    length = len(array) - 1

    for i in range(length):
        for j in range(length):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    return array

array = [5, 2, 4, 1, 3]
print(bubble_sort(array))
