## Happy Number

def is_happy(num):
    '''
    Function that returns True if number is happy, False otherwise.

    Arguments:
    num -- integer value

    Returns:
    <bool> -- True if happy, False otherwise
    '''

    while num != 1 and num != 4:
        num = [int(x) for x in str(num)]

        num = sum(map(lambda i: i*i, num))
    
    if num == 1:
        return True
    else:
        return False

num = 13

print(is_happy(num))
