'''
Smallest window that contains all characters of string itself.

Given a string, find the smallest window length with all distinct 
characters of the given string. For eg. str = “aabcbcdbca”, then 
the result would be 4 as of the smallest window will be “dbca” .

Using Sliding Window
'''

def find_substring(string):
    '''
    Function to find the smallest substring.

    Argument:
    string -- str

    Returns:
    str, having smallest size.
    '''
    hash_str = [0] * 256

    dist_chars = len(set([item for item in string]))
    min_length = float('inf')

    count, start = 0, 0
    for j in range(len(string)):
        hash_str[ord(string[j])] += 1

        if hash_str[ord(string[j])] == 1:
            count += 1
        
        if count == dist_chars:
            while hash_str[ord(string[start])] > 1:
                if hash_str[ord(string[start])] > 1:
                   hash_str[ord(string[start])] -= 1
                start += 1

            len_window = j - start + 1
            if len_window < min_length:
                start_index = start
                min_length = len_window  
            
    return string[start_index: start_index + min_length]

string = 'aaab'
print(find_substring(string))
