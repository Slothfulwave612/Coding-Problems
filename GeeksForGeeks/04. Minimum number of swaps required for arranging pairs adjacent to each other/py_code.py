## Minimum number of swaps required for arranging pairs adjacent to each other

def count_min_swaps(array, pairs):
    '''
    This function will count minimum number of swaps.

    Argument:
    array -- list, containing integer values.
    pairs -- list, pair of each value.

    Returns:
    count -- int, minimum number of swaps.
    '''
    length = len(array)
    i = 0
    count = 0

    while i != length:
        c = 0
        for j in range(len(pairs)):
            if pairs[j] == array[i]:
                if j == len(pairs) - 1 and len(pairs) % 2 != 0:
                    c = 1
                elif j % 2 == 0:
                    partner = pairs[j + 1]
                elif j % 2 != 0:
                    partner = pairs[j - 1]
                break
        
        if c != 1:
            if array[i+1] != partner:
                for k in range(i+1, length):
                    if array[k] == partner:
                        pos = k
                array[i+1], array[pos] = array[pos], array[i+1]
                count += 1
            i += 2
        
        elif c == 1:
            if i != len(array) - 1:
                array[i], array[j] = array[j], array[i]
                count += 1
                # i += 2
            else:
                i += 1
                
    return count

pairs = [4, 9, 5, 11, 10, 1, 2, 6, 7, 3, 8] 
array = [4, 8, 5, 7, 11, 3, 10, 2, 1, 6, 9]

print(count_min_swaps(array, pairs))
