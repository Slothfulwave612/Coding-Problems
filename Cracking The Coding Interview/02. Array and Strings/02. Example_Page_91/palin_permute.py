'''
Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rea rrangement of letters. The palindrome does not need to be limited to just dictionary words.

EXAMPLE
Input: Tact Coa
Output: True (permutations: "taco cat". "atco cta". etc.)
'''

def palin_permute(string):
    '''
    Function to check if a string is a permutation of a palindrome.

    Argument:
    string -- str

    Returns:
    True or False
    '''
    hash_map = {}

    for word in string:
        if word != ' ':
            if hash_map.get(word) == None:
                hash_map[word] = 1
            else:
                hash_map[word] += 1
            
    odd_count = 0

    for index in hash_map:
        if hash_map[index] % 2 != 0:
            odd_count += 1
            if odd_count == 2:
                return False
    
    return True

string = 'tact coa'
print(palin_permute(string))
