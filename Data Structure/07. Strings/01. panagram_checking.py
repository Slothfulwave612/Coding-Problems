## Pangram Checking

def is_panagram(string):
    '''
    Function to check whether a given string is Panagram or not

    Argument:
    string -- str

    Returns:
    True -- if string is panagram or not.
    '''
    alphabet = [False] * 26

    for word in string:
        if word.lower() != ' ':
            alphabet[ord(word) - ord('a')] = True
    
    for item in alphabet:
        if item == False:
            return False
    
    return True

string = 'The quick brown fox jumps over the little lazy dog'

print(is_panagram(string))
