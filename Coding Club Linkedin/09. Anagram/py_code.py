## Anagram

def is_anagram(string1, string2):
    '''
    The function returns True if the string 1 is anagram of other string else False

    Arguments:
    string1: a Python string,
    string2: a Python string.

    Returns:
    <bool> value: True or False
    '''

    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

string1 = 'allergy'
string2 = 'allergic'

print(is_anagram(string1, string2))