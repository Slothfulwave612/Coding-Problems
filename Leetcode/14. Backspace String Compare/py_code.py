## Backspace String Compare

def main_command(string):
    '''
    The function will return a stack.
    
    Arguments:
    string -- a string

    Returns:
    stack -- a stack
    '''
    stack = []
        
    for item in string:
        if item != '#':
            stack.append(item)
        elif item == '#' and len(stack) > 0:
            stack.pop()
    return stack
        
def backspaceCompare(S, T):
    '''
    The function returns True if both string after pop opeartions are same,
    otherwise False.

    Arguments:
    S -- a string 
    T -- a string

    Retuns:
    <bool> -- True or False
    '''
    stack_S = main_command(S)
    stack_T = main_command(T)
        
    if stack_S == stack_T:
        return True
    else:
        return False

S = "ab#c"
T = "ad#c"

print(backspaceCompare(S, T))