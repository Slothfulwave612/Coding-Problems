'''
Remove all adjacent duplicates
Given a string, remove adjacent 
duplicate characters from the string. The output string should not have any adjacent duplicates. See following examples.

Examples:

Input: azxxzy
Output: ay
First “azxxzy” is reduced to “azzy”.
The string “azzy” contains duplicates,
so it is further reduced to “ay”.

Input: geeksforgeeg
Output: gksfor
First “geeksforgeeg” is reduced to
“gksforgg”. The string “gksforgg”
contains duplicates, so it is further
reduced to “gksfor”.

Input: caaabbbaacdddd
Output: Empty String

Input: acaaabbbacdddd
Output: acac
'''

def remove(string):
    '''
    Function to remove all adjacent duplicates.

    Arguments:
    string -- str.

    Returns:
    stack -- list, of character.
    '''
    stack = []
    last_pop = ''
    
    for item in string:
        if len(stack) == 0 or (stack[-1] != item and item != last_pop):
            stack.append(item)
        
        elif stack[-1] == item or stack[-1] == last_pop:
            last_pop = stack.pop()
    
    return ''.join(elem for elem in stack)

string1 = "geeksforgeeg"
print(remove(string1))
  
string2 = "azxxxzy"
print(remove(string2))
  
string3 = "caaabbbaac"
print(remove(string3))
  
string4 = "gghhg"
print(remove(string4))
  
string5 = "aaaacddddcappp"
print(remove(string5))
  
string6 = "aaaaaaaaaa"
print(remove(string6))
  
string7 = "qpaaaaadaaaaadprq"
print(remove(string7))
  
string8 = "acaaabbbacdddd"
print(remove(string8))
  
string9 = "acbbcddc"
print(remove(string9))
