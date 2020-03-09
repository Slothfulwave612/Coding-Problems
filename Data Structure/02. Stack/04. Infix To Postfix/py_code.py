## Infix to Postfix using stack

def is_operator(item):
    '''
    This function checks whether a given item is an operator or not.
    
    Arguments:
    item -- string value
    
    Returns:
    bool -- True: if item is an operator
            False: otherwise.
    '''
    
    if item == '^' or item == '*' or item == '/' or item == '+' or item =='-':
        return True
    else:
        return False
        
def operator_precedence(item):
    '''
    This function returns the precedence of the operator.
    
    Argument:
    item -- operator
    
    Return:
    int -- 3, 2, 1 precedence level
    '''
    if item == '^':
        return 3
    elif item == '/' or item =='*':
        return 2
    elif item == '+' or item =='-':
        return 1

def infix_to_postfix(infix):
    '''
    This function converts infix expression to postfix expression.
    
    Arguments:
    infix -- str, containing infix operation.
    
    Returns:
    str or bool -- str when the expression is converted to postfix.
                   False when the infix expression is invalid.
    '''
    
    stack = []
    postfix = []
    
    stack.append('(')
    infix += ')'
    
    for item in infix:
        if item == '(':
            stack.append(item)
        
        elif str.isdigit(item) or str.isalpha(item):
            postfix.append(item)
        
        elif is_operator(item) == True:
            x = stack.pop()
            while is_operator(x) == True and operator_precedence(x) >= operator_precedence(item):
                postfix.append(x)
                x = stack.pop()
            stack.append(x)
            stack.append(item)
        
        elif item == ')':
            x = stack.pop()
            while x != '(':
                postfix.append(x)
                x = stack.pop()
    
    if len(stack) > 0:
        return False
    else:
        return postfix

infix = 'A*(B+D)/E-F-(G+H/K)'
print(infix_to_postfix(infix))
