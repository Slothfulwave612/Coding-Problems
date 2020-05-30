## Minimum number of swaps required to sort an array | Set 2

def count_swaps(array):
    '''
    Function to count minimum number of swaps required to 
    sort the array.

    Argument:
    array -- list, containing the integers.

    Returns:
    count -- int, total number of swaps.
    '''
    count = 0

    for i in range(len(array)):
        pos = i

        for j in range(i+1, len(array)):
            if array[pos] > array[j]:
                pos = j
            
        if pos != i:
            array[i], array[pos] = array[pos], array[i]
            count += 1
        
    print(array)
    return count

array_1 = [4, 3, 2, 1]
print(count_swaps(array_1))

array_2 = [3, 5, 2, 4, 6, 8]
print(count_swaps(array_2))
