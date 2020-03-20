## Count of elements which are not at the correct position

def count_elements(array):
    '''
    This function counts total number of integers that are not in correct position.

    Argument:
    array -- list, containing integer values.

    Returns:
    count -- int
    '''
    cpy_array = array.copy()

    cpy_array.sort()

    count = 0
    for i in range(len(cpy_array)):
        if array[i] != cpy_array[i]:
            count += 1
    
    return count

array = [1, 2, 6, 2, 4, 5]
print(count_elements(array))
