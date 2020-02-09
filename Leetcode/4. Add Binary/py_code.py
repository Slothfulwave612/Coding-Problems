## Add binary

def addBinary(a, b):
    '''
    The function adds two binary numbers a and b.

    Arguments:
    a -- string containing binary digits
    b -- string containing binary digits

    Returns:
    c -- the result of a + b
    '''
    
    maxim = max(len(a), len(b))
    
    a = a.zfill(maxim)
    b = b.zfill(maxim)

    c = ''
    ## summation of a and b will be stored here

    carry = 0   ## initial carry

    for i in range(maxim-1, -1, -1):
        summ = int(a[i]) + int(b[i]) + carry
        carry = summ // 2
        c = c + str(summ % 2)
    
    if carry == 1:
        c = c + str(1)

    return c[::-1]

a1, b1 = '11', '1'
a2, b2 = '10', '100'

print(addBinary(a1,b1))
print(addBinary(a2,b2))