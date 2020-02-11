## Full Pyramid

def full_pyramid(height):
    '''
    Print the pattern of full pyramid

    Arguments:
    height -- height of the pyramid

    Returns:
    <None>
    '''
    for i in range(1, height + 1):
        for j in range(i, height):
            print(' ', end='')
        for k in range(1, i + 1):
            print('*', end=' ')
        print()

full_pyramid(10)