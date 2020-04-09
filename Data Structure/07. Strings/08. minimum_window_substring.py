'''
Find the smallest window in a string containing all characters of another string

Given two strings string1 and string2, the task is to find the smallest substring 
in string1 containing all characters of string2 efficiently.

Examples:
Input: string = “this is a test string”, pattern = “tist”
Output: Minimum window is “t stri”
Explanation: “t stri” contains all the characters of pattern.
'''

def find_substring(string_1, string_2):
    '''
    Function to find the smalled window in string_1.

    Arguments:
    string_1 -- str, the original string from when the window is to be found.
    string_2 -- str, the characters to be found in the string_1.

    Returns:
    str, the smallest window in a string.
    '''
    if len(string_2) > len(string_1):
        return 'No window can be found.'
    
    hash_pattern = [0] * 256
    hash_string = [0] * 256
    ## 256, for all the ASCII characters

    for char in string_2:
        hash_pattern[ord(char)] += 1
    
    start, start_index, min_length = 0, -1, float('inf')

    count = 0
    for j in range(len(string_1)):
        hash_string[ord(string_1[j])] += 1

        if hash_pattern[ord(string_1[j])] != 0 and hash_string[ord(string_1[j])] <= hash_pattern[ord(string_1[j])]:
            count += 1

        if count == len(string_2):
            while hash_pattern[ord(string_1[start])] == 0 or hash_pattern[ord(string_1[start])] < hash_string[ord(string_1[start])]:
                if hash_string[ord(string_1[start])] > hash_pattern[ord(string_1[start])]:
                    hash_string[ord(string_1[start])] -= 1
                start += 1                

            len_window = j - start + 1
            if len_window < min_length :
                start_index = start
                min_length = len_window
    
    if start_index == -1:
        return 'No window found.'
    
    return string_1[start_index: start_index + min_length]

string_1 = 'this is a test string'
string_2 = 'tist'

print(find_substring(string_1, string_2))
