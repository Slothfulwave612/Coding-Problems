## Round the given number to nearest multiple of 10

def round_num(num):
    '''
    Function to round an integer to nearest 10.

    Argument:
    num -- int.

    Returns:
    round to nearest 10.
    '''
    result = num % 10

    if result >= 5:
        num += (10 - result)
    else:
        num -= result
    
    return num

print(round_num(4722))

print(round_num(38))

print(round_num(10))
