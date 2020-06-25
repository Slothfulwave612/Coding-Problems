## Longest Substring With No Duplicates

def count_length(string):
    '''
    Function to count the length of longest substring
    having no duplicates.

    Argument:
    string -- str, containing characters.

    Returns:
    count -- int, the length of substring with no duplicates.
    '''
    if len(string) == 0:
        return 0

    hash_map = [0] * 256
    length = len(string)
    hash_map[ord(string[0])] = 1
    count = 1
    i, j = 0, 0

    while j != length - 1:
        if hash_map[ord(string[j+1])] == 0:
            hash_map[ord(string[j+1])] = 1
            j += 1
            count = max(count, j-i+1)
        else:
            hash_map[ord(string[i])] -= 1
            i += 1
    
    return count

string = 'abrexzex'
print(count_length(string))
