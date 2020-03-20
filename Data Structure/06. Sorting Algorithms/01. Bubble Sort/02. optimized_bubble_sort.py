## Optimized Bubble Sort Implementation

def opt_bub_sort(array):
    '''
    This function performs bubble sort(optimized) on a given array.

    Argument:
    array -- list, containing integer values.

    Returns:
    array -- list, sorted in ascending order.
    '''
    length = len(array)

    for i in range(length - 1):
        swapped = False
        for j in range(0, length - i - 1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if swapped == False:
            break
    
    return array

array = [5, 4, 2, 3, 1]
print(opt_bub_sort(array))
