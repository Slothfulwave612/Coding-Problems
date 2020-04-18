'''
Is Unique: Implement an algorithm to determine if a string has all unique characters.
'''

def check_unique(string):
    '''
    Function to check whether the string has all unique characters or not.

    Arguments:
    string -- str

    Returns:
    True -- if string has all unique characters
    False -- otherwise
    '''
    hash_table = {}

    for word in string:
        if word != ' ':
            if hash_table.get(word) == None:
                hash_table[word] = 1
            else:
                hash_table[word] += 1
        
    len_hash = len(hash_table)
    summed_result = 0

    for i in hash_table:
        summed_result += hash_table[i]
    
    if summed_result - len_hash == 0:
        return True
    else:
        return False
    
string = 'sloth612'
print(check_unique(string))
