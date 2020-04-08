## Check Whether a number is Duck Number or not

def duck_number(num):
    '''
    Function to check whether the given number is duck number or not.

    Argument:
    num -- string, number to be checked.
    '''
    if num[0] != '0':
        for i in range(1, len(num)):
            if num[i] == '0':
                return True
        return False
    else:
        return False

num = '707069'
result = duck_number(num)

if result == True:
    print('This is a duck number.')
else:
    print('This is not a duck number.')
