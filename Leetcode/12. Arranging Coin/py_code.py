## Arranging Coin

import math     ## math module

def arrange_coins(num):
    '''
    The function returns the required value.

    Arguments:
    num -- integer value

    Returns:
    <int> -- required value
    '''
    
    return int((math.sqrt(8 * num + 1) - 1) / 2)

n1 = 5
n2 = 8

print(arrange_coins(n1))
print(arrange_coins(n2))