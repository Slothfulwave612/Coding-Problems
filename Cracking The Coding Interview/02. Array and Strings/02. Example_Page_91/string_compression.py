'''
String Compression: Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
'''

def string_compression(string):
    '''
    Function to compress the string.

    Argument:
    string -- str

    Returns:
    compressed_str -- str
    False -- if string cannot be compressed.
    '''
    compressed_str = ''
    count = 0

    for i in range(0, len(string)):
        count += 1
        if i + 1 >= len(string) or string[i] != string[i+1]:
            compressed_str += string[i] + str(count)
            count = 0

    if len(compressed_str) < len(string):
        return compressed_str
    else:
        return False
    
string = 'aabcccccaaad'
print(string_compression(string))
