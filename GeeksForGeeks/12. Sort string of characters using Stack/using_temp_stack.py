## Sort strings of characters using Stack

def sort_string_stack(string):
    '''
    This function will sort a string of characters using Stack.

    Argument:
    string -- str, a string.

    Returns:
    tmp_string -- str, containing character of stack in sorted order.
    '''
    stack = [elem for elem in string]
    tmp_stack = []

    while stack != []:
        temp = stack.pop()

        while tmp_stack != [] and ord(tmp_stack[-1]) > ord(temp):
            element = tmp_stack.pop()
            stack.append(element)
        
        tmp_stack.append(temp)

    tmp_string = ''.join([elem for elem in tmp_stack])

    return tmp_string

string = 'hello395world216'
print(sort_string_stack(string))    
