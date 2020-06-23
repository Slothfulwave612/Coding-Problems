# Minimum adjacent swap required to Sort Binary array

def count_swaps(array):
    '''
    Function to count minimum number of swap to sort 
    the binary array.

    Argument:
    array -- list, containing 0s and 1s.

    Returns:
    count -- int, the minimum number of swap.
    '''
    i = len(array) - 1
    count, check = 0, 0

    while i != 0:
        if array[i] == 0:
            if array[i - 1] == 1:
                array[i], array[i - 1] = array[i - 1], array[i]
                i += (check)
                check = 0
                count += 1
                continue

            else:
                check += 1
        i -= 1

    print(array)
    return count

array = [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
print(count_swaps(array))
    
