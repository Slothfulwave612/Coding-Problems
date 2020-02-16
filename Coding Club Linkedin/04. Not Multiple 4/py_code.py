## Not Multiple 4

def not_multiple_4(num):
    '''
    Returns numbers 3N+2 which are not a multiple of 4

    Arguments:
    num -- integer value

    Returns:
    <None>
    '''
    
    i, c = 1, 0

    while c != num:
        num_gen = (3 * i) + 2

        if num_gen % 4 != 0:
            print(num_gen, end=' ')
            c += 1
        i += 1

num = 10
not_multiple_4(num)