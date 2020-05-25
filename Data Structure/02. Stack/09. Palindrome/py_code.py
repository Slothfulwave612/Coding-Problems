'''
Given an array of characters formed with a’s and b’s. The string is marked with
special character X which represents the middle of the list (for example:
ababa...ababXbabab baaa). Check whether the string is palindrome.
'''

def check_palindrome(string):
    '''
    Function to check whether a string is palindrome or not.

    Argument:
    string -- str

    Return:
    bool -- True, if palindrome
            False, otherwise.
    '''
    i, j = 0, len(string) - 1

    while True:
        if string[i] == string[j]:
            if string[i] == 'X':
                return True
            i += 1
            j -= 1
        
        else:
            return False

string_1 = 'abbaXabba'
string_2 = 'abcdXdcba'
string_3 = 'slothXful'
string_4 = 'slothXtols'

print('For {0}, result = {1}'.format(string_1, check_palindrome(string_1)))
print('For {0}, result = {1}'.format(string_1, check_palindrome(string_2)))
print('For {0}, result = {1}'.format(string_1, check_palindrome(string_3)))
print('For {0}, result = {1}'.format(string_1, check_palindrome(string_4)))
