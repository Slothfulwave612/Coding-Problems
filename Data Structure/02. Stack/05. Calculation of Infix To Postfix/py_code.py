## Calculation of postfix operations

def is_operator(item):
    '''
    This function will tell whether item is operator or not.

    Argument:
    item -- string.

    Returns:
    bool -- True: if the item is an operator.
            False: otherwise.
    '''
    if item == '*' or item == '/' or item == '+' or item == '-':
        return True
    else:
        return False

def cal_postfix(postfix):
    '''
    This function calculates the postfix expressions.

    Arguments:
    postfix -- string, having the postfix operation.

    Returns:
    int -- solution of the postfix operation.
    '''

    stack = []
    postfix = postfix.split(' ')

    for item in postfix:
        if str.isdigit(item):
            stack.append(item)
        
        elif is_operator(item):
            opr_two = int(stack.pop())
            opr_one = int(stack.pop())
            
            if item == '*':
                result = (opr_one * opr_two)
            
            elif item == '/':
                result = (opr_one / opr_two)

            elif item == '+':
                result = (opr_one + opr_two)

            elif item == '-':
                result = (opr_one - opr_two)
            stack.append(result)

    return stack[-1]

postfix = '6 5 2 * 4 + +'
print(cal_postfix(postfix))
