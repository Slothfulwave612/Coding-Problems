## Reverse a stack using recursion

def reverse_stack(stack):
    '''
    This is a recursive function and prints stack in reverse.

    Arguments:
    stack -- list, containing integer values.
    '''
    if stack != []:
        print(stack.pop())
        return reverse_stack(stack)
    else:
        return 
    
stack = [32, 12, 54, 112, 43 , 23]
reverse_stack(stack)
