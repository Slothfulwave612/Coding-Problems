## Sort a stack using recursion

def sort_stack(stack):
    '''
    This function will sort stack using the concept of recursion.

    Argument:
    stack -- list, containing integer values in unsorted order.

    Returns:
    stack -- list, containing integer values in sorted order.
    '''
    if stack != []:
        temp = stack.pop()
        sort_stack(stack)
        sort_insert(stack, temp)

    return stack

def sort_insert(stack, temp):
    '''
    This function will check and sort the values.

    Arguments:
    stack -- list, containing integer values or may be empty.
    temp -- int, the value to be inserted in a sorted manner.
    '''

    if stack == [] or temp > stack[-1]:
        stack.append(temp)
    else:
        element = stack.pop()
        sort_insert(stack, temp)
        stack.append(element)

stack = [5, 2, 3, 1, 4]
print(sort_stack(stack))
