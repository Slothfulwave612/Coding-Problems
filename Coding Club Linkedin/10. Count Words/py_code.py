## Count Words

def total_words(string):
    '''
    The function counts total number of words in a string.

    Arguments:
    string -- a string.

    Returns:
    tot_words -- total number of words in the string.
    '''

    tot_word = 0

    for word in string:
        if word == ' ':
            tot_word += 1
    
    return tot_word + 1

string1 = 'this is a sample string'
string2 = 'i am sloth'
string3 = 'Hey'

print(total_words(string1))
print(total_words(string2))
print(total_words(string3))