'''
Example: Design an algorithm to print all permutations of a string. For simplicity, assume all characters
are unique.

Below are the permutations of string ABC.
ABC ACB BAC BCA CBA CAB
'''

def all_permute(array, front, rare):
    '''
    Function to print all permutation of a given string.

    Arguments:
    array -- list, containing all characters of the given string.
    front -- int, front of the array.
    rare -- int, rare of the array.
    '''
    if front == rare:
        print(''.join(array))

    else:
        for i in range(front, rare+1):
            array[front], array[i] = array[i], array[front]
            all_permute(array, front+1, rare)
            array[i], array[front] = array[front], array[i]     ## backtrack
        
string = 'ABCA'
array = list(string)
all_permute(array, 0, len(string)-1)
