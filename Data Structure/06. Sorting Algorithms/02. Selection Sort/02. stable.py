## Stable Selection Sort Implementation

def stable_sel_sort(array):
    '''
    This function performs selection sort(stable) on a given array.

    Argument:
    array -- list, containing integer values.

    Returns:
    array -- list, sorted in ascending order.
    '''
    length = len(array)

    for i in range(length):
        min_indx = i

        for j in range(i + 1, length):
            if array[min_indx] > array[j]:
                min_indx = j
        
        key = array[min_indx]
        while min_indx > i:
            array[min_indx] = array[min_indx - 1]
            min_indx -= 1
        array[i] = key
    
    return array

array = [5, 2, 3, 1, 4, 3]
print(stable_sel_sort(array))
