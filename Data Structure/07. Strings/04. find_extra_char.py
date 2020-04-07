## Find one extra character in a string

def one_extra(string_1, string_2):
    '''
    Function to find extra characters in a string.

    Arguments:
    string_1 -- str
    string_2 -- str, containing extra characters.
    '''
    hash_table = {}

    for word in string_1:
        hash_table[word] = 1
    
    for word in string_2:
        if hash_table.get(word) == None or hash_table.get(word) == 2:
            print(word, end=' ')
        else:
            hash_table[word] = hash_table[word] + 1


string_1 = 'kxml'
string_2 = 'klxml'

one_extra(string_1, string_2)
