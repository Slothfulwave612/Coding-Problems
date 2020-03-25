## Sort string of characters using Stack

def sort_stack(stack):
    '''
    This function will sort the given stack.

    Argument:
    stack -- list, string of character in unsorted order.

    Returns:
    string -- string, string in sorted order.
    '''
    if stack != []:
        temp = stack.pop()
        sort_stack(stack)
        sort_inserted(stack, temp)

    string = ''.join([elem for elem in stack])
    return string

def sort_inserted(stack, temp):
    '''
    This function will sort the character in the stack.

    Arguments:
    stack -- list, containing characters or maybe empty.
    temp -- str, the poped character.
    '''
    if stack == [] or ord(temp) > ord(stack[-1]):
        stack.append(temp)
    else:
        element = stack.pop()
        sort_inserted(stack, temp)
        stack.append(element)

string = 'hello395world216'
stack = [elem for elem in string]

print(sort_stack(stack))
