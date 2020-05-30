## Minimum number of swaps required to sort an array of first N number

def count_swaps(array):
    '''
    Function to count number of swaps required to sort the array.

    Argument:
    array -- list, containing integers.

    Returns:
    count -- int, total number of swaps required.
    '''
    i, count = 0, 0

    while i != len(array) - 1:
        if array[i] != i + 1:
            while array[i] != i + 1:
                temp = array[i]
                array[i] = array[array[i] - 1]
                array[temp - 1] = temp
                count += 1
        
        i += 1
    print(array)

    return count

array_1 = [7, 1, 3, 2, 4, 5, 6]
print(count_swaps(array_1))

array_2 = [2, 3, 4, 1, 5]
print(count_swaps(array_2))
