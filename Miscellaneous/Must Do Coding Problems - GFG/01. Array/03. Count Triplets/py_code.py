## Count Triplets such that one of the numbers can be written as sum of the other two.

def count_triplets(array):
    '''
    Function will count the required triplets.

    Argument:
    array -- list, containing integers

    Retunrs:
    count -- int, containing number of triplets.
    '''
    length = len(array)
    
    max_val = max(array)

    freq = [0 for i in range(max_val + 1)]

    for i in range(length):
        freq[array[i]] += 1

    count = 0

    count += (freq[0] * (freq[0] - 1) * (freq[0] - 2)) // 6

    for i in range(1, max_val + 1):
        count += (freq[0] * freq[i] * (freq[i] - 1)) // 2
    
    for i in range(1, (max_val // 2) + 1):
        count += (freq[i] * (freq[i] - 1) * freq[2*i]) // 2
    
    for i in range(1, max_val + 1):
        for j in range(i+1, max_val - i + 1):
            count += (freq[i] * freq[j] * freq[i+j])
    
    return count

array = [1, 1, 1, 2, 2]
print(count_triplets(array))

