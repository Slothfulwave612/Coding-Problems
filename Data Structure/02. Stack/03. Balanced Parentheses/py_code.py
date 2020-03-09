## Check for balanced parentheses

def check_brckt(item, last):
    '''
    The function will check brackets.
    
    Arguments:
    item -- str, closed bracket ) or } or ]
    
    Returns:
    bool -- True: if stack's top is opening bracket of respective closed bracket, i.e. ) matched with (
            False: otherwise
    '''
    if item == ')' and last == '(':
        return True
    elif item == '}' and last == '{':
        return True
    elif item == ']' and last == '[':
        return True
    else:
        return False

def check_balanced_parentheses(string):
    '''
    The function will check for balanced parentheses.
    
    Arguments:
    string -- str, containing expression
    
    Returns:
    bool -- True: if parentheses are balanced.
            False: otherwise.
    '''
    
    stack = []
    
    for item in string:
        if item == '(' or item == '[' or item =='{':
            stack.append(item)
        elif item == ')' or item == ']' or item == '}':
            if len(stack) == 0 or check_brckt(item, stack[-1]) == False:
                return False
            else:
                stack.pop()
    
    if len(stack) == 0:
        return True
    else:
        return False
        
string = '[(a+b) * (c+d}]'
print(check_balanced_parentheses(string))

string = '[[][][][][][][][][]]'
print(check_balanced_parentheses(string))

string = '({{{}}})[[[[]]]]()'
print(check_balanced_parentheses(string))
