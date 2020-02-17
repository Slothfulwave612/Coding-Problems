## Divisor
import math

def divisor(num):
    '''
    Prints all the divisors of the number.

    Arguments:
    num -- integer value

    Returns:
    <None>
    '''

    i = 1

    while i <= math.sqrt(num):
        if num % i == 0:
            if num // i == i:
                print(i, end=' ')
            else:
                print(i, num // i, end=' ')
        i += 1

num = 100
divisor(num)