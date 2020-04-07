## Missing characters to make a string Pangram

def missing_char(string):
    '''
    Function to find missing characters to make a string Panagram.

    Argument:
    string -- str

    Returns:
    all characters required to make the string panagram.
    '''
    alphabet = [False] * 26

    for word in string:
        if word.lower() != ' ':
            alphabet[ord(word) - ord('a')] = True
    
    count = 0
    for item in range(len(alphabet)):
        if alphabet[item] == False:
            print(chr(ord('a') + item), end='')
            count = 1
    print()

    if count == 0:
        print('String is a panagram')

string = 'welcome to geeksforgeeks'
missing_char(string)
