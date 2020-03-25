## Sort a stack using temporary stack

def sort_stack(stack):
    '''
    This function will sort the given stack.

    Argument:
    stack -- list, containing integer values in unsorted order.

    Returns:
    tmp_stack -- list, containing integer values in sorted order.
    '''
    tmp_stack = []

    while stack != []:
        temp = stack.pop()

        while tmp_stack != [] and tmp_stack[-1] > temp:
            element = tmp_stack.pop()
            stack.append(element)          
        
        tmp_stack.append(temp)
    
    return tmp_stack

stack = [4, 2, 6, 3, 1, 5]
print(sort_stack(stack))
