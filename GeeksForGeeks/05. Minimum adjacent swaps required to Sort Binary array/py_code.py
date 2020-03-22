## Minimum adjacent swaps required to Sort Binary array

def count_min_swaps(array):
    '''
    This function will count minimum swaps to sort the array.

    Argument:
    array -- list, containing integer values.

    Returns:
    count -- int, minimum number of swaps.
    '''
    length = len(array)
    count = 0
    i = length - 1
    check = 0
    
    while i != 0:
        if array[i] == 0:
            if array[i-1] == 1:
                temp = array[i-1]
                array[i-1] = array[i]
                array[i] = temp
                count += 1
                i += (check + 1)
                check = 0
            else:
                check += 1
        i -= 1

    print(array)
    return count

array = [0, 0, 1, 0, 1, 0, 1, 1]
print(count_min_swaps(array))
