'''
Check Permutation: Given two strings, write a method to decide if one is a permutation of the
other.
'''

def check_permute(string_1, string_2):
    '''
    Function to check one string is permutation of the other
    or not.

    Arguments:
    string_1 -- str
    string_2 -- str

    Returns:
    True -- if the string is the permutation of the other.
    False -- otherwise.
    '''
    if len(string_1) != len(string_2):
        return False

    hash_table = {}

    for word in string_1:
        if hash_table.get(word) == None:
            hash_table[word] = 1
        else:
            hash_table[word] += 1
        
    for word in string_2:
        if hash_table.get(word) != None:
            hash_table[word] -= 1
    
    summed_result = 0

    for i in hash_table:
        summed_result += hash_table[i]

    if summed_result == 0:
        return True
    else:
        return False
    
string_1 = 'abbcde'
string_2 = 'edcbab'
print(check_permute(string_1, string_2))
