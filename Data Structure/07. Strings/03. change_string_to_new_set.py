## Change string to a new character set

def change_string(char_set, string):
    '''
    Function to change the string.

    Arguments:
    char_set -- string of characters(a new alphabet system).
    string -- str, string to be converted.
    
    Returns:
    string in our alphabet system.
    '''
    hash_table = {}

    for word in range(len(char_set)):
        hash_table[ord(char_set[word]) - ord('a')] = chr(ord('a') + word)
    
    for word in string:
        print(hash_table[ord(word) - ord('a')], end='')
    print()

char_set = 'qwertyuiopasdfghjklzxcvbnm'

change_string(char_set, 'utta')
change_string(char_set, 'egrt')
