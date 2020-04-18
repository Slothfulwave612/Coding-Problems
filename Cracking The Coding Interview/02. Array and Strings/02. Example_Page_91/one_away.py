'''
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
EXAMPLE
pale, ple -) true
pales, pale -) true
pale, bale -) true
pale, bae -) false 
'''

def check_string(string_1, string_2):
    '''
    Function to check the given contiditons

    Arguments:
    string_1 -- str
    string_2 -- str

    Returns:
    True or False
    '''
    if len(string_1) - 1 == len(string_2):
        #remove
        return remove_insert(string_1, string_2, 1)
    elif len(string_1) == len(string_2) - 1:
        # insert
        return remove_insert(string_1, string_2, 2)
    elif len(string_1) == len(string_2):
        # replace
        return replace(string_1, string_2)
    else:
        return False

def remove_insert(string_1, string_2, value):
    '''
    Function to check remove/insert.

    Arguments:
    string_1 -- str
    string_2 -- str
    value -- 1 if it's for remove 
             2 if it's for insert
            
    Returns:
    True or False
    '''
    index_1 = 0
    index_2 = 0
    count = 0

    while index_1 != len(string_1) and index_2 != len(string_2):
        if string_1[index_1] != string_2[index_2]:
            count += 1
            if count == 2:
                return False
            if value == 1:
                index_1 += 1
            if value == 2:
                index_2 += 1
        
        else:
            index_1 += 1
            index_2 += 1
    
    if count == 1:
        return True
    else:
        return False

def replace(string_1, string_2):
    '''
    Function to check the replace condition

    Arguments:
    string_1 -- str
    string_2 -- str

    Returns:
    True or False
    '''
    index_1 = 0
    index_2 = 0  
    count = 0

    while index_1 != len(string_1) and index_2 != len(string_2):
        if string_1[index_1] != string_2[index_2]:
            count += 1
            if count == 2:
                return False
        index_1 += 1
        index_2 += 1
    
    if count == 1:
        return True
    else:
        return False

string_1 = 'pale'
string_2 = 'pasle'

print(check_string(string_1, string_2))
