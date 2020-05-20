'''
Reverse a stack.
'''

def create_stack():
    '''
    Function to create an empty stack.

    Returns:
    stack -- list, an empty stack.
    '''
    stack = []
    return stack

def push(stack, data):
    '''
    Function to push the element into the stack.

    Arguments:
    stack -- list, represents the stack.
    data -- int, data to be added to the stack.
    '''
    stack.append(data)

def pop(stack):
    '''
    Function to delete the topmost element from the stack.

    Argument:
    stack -- list, represents the stack.

    Returns:
    int, the topmost element.
    '''
    if len(stack) == 0:
        print('Stack Underflow')
        return None
    
    return stack.pop()

def insert(stack, data):
    '''
    Function to insert the data while reversing.

    Arguments:
    stack -- list, repersents the stack.
    data -- int, data to be added.
    '''
    if len(stack) == 0:
        push(stack, data)
    else:
        temp = stack.pop()
        insert(stack, data)
        push(stack, temp)

def reverse(stack):
    '''
    Function to reverse the stack.

    Argument:
    stack -- list, represents the stack.
    '''
    if len(stack) == 0:
        return
    temp = pop(stack)
    reverse(stack)
    insert(stack, temp)

def display(stack):
    '''
    Function to display the stack.

    Argument:
    stack -- list, represents the stack.
    '''
    if len(stack) == 0:
        print('Stack Underflow')
        return None
    
    for i in range(len(stack) - 1, -1, -1):
        print(stack[i], end=' ')
    print()

stack = create_stack()
push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)

display(stack)

reverse(stack)

display(stack)
