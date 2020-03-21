## Minimum number of swaps required to sort an array of first N number

def count_min_swaps(array):
    '''
    This function will count the mininum swaps required to sort the array

    Argument:
    array -- list, containing integer values.

    Returns:
    count -- int, minimum swaps required.
    '''
    length = len(array)
    count = 0

    for i in range(length):
        if array[i] != i + 1:
            while array[i] != i + 1:
                temp = array[array[i] - 1]
                array[array[i] - 1] = array[i]
                array[i] = temp
                count += 1
    return count

array = [3, 4, 5, 1, 2]
print(count_min_swaps(array))
