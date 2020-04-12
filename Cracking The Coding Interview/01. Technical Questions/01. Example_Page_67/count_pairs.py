'''
Example: Given an array of distinct integer values, count the number of pairs of integers that
have difference k. For example, given the array {1, 7, 5, 9, 2, 12, 3} and the difference
k = 2, there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9).
'''

def find_pairs(array, k):
    '''
    Function to find the required pair count.
    '''
    count = 0

    hash_map = {}

    for num in array:
        hash_map[num] = True
    
    for num in array:
        if hash_map.get(num - k) == True:
            print(f'({num}, {num - k})', end=' ')
            count += 1
    print()

    return count

array = [1, 5, 3, 4, 2]
k = 3

print(f'Total Pairs: {find_pairs(array, k)}')
