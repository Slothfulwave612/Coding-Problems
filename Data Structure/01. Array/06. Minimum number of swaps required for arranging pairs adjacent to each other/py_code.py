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
    arr_len, pair_len = len(array), len(pairs)
    count = 0

    for i in range(0, arr_len, 2):
        valid = 0

        for j in range(0, pair_len):
            if array[i] == pairs[j]:

                if j == pair_len - 1 and pair_len % 2 != 0 and array[i] == pairs[j]:
                    valid = 1

                elif j % 2 == 0:
                    partner = pairs[j + 1]
                
                else:
                    partner = pairs[j - 1]
                
                break

        if valid == 0 and array[i + 1] != partner:
            for k in range(i + 2, len(array)):
                if array[k] == partner:
                    count += 1
                    array[i + 1], array[k] = array[k], array[i + 1]

    return count

pairs = [0, 3, 6, 1, 5, 4, 2] 
array = [0, 3, 5, 6, 4, 1, 2] 

print(count_min_swaps(array, pairs))
