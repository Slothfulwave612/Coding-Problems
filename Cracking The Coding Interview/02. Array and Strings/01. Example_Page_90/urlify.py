'''
URLify: Write a method to replace all spaces in a string with '%20: You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string. (Note: If implementing in Java, please use a character array so that you can
perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"
'''

def urlify(array, orig_len):
    '''
    Function to replace spaces with '%20'.

    Arguments:
    array -- list, array of characters
    orig_len -- int, length of the original string.

    Return:
    array -- , listarray of characters(with %20 in it)
    '''
    spc_count = 0
    for word in string:
        if word == ' ':
            spc_count += 1
        elif word == '\n':
            break
    
    req_spc = spc_count * 2
    index = orig_len + req_spc

    for i in range(orig_len - 1, -1, -1):
        if array[i] == ' ':
            array[index - 1] = '0'
            array[index - 2] = '2'
            array[index - 3] = '%'
            index -= 3

        else:
            array[index - 1] = array[i]
            index -= 1
    
    return array[: orig_len + req_spc]

string = 'Mr John Smith'
length = len(string)
string += '\n'* 10
array = list(string)

print(urlify(array, length))
