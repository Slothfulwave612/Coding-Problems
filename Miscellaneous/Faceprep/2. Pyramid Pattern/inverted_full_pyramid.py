## Inverted Full Pyramid

def inverted_full_pyramid(height):
    '''
    Print the pattern of inverted full pyramid

    Arguments:
    height -- height of the pyramid

    Returns:
    <None> 
    '''
    for i in range(height, 0, -1):
        for j in range(i, height):
            print(' ', end='')
        for k in range(1, i + 1):
            print('*', end=' ')
        print()

inverted_full_pyramid(10)