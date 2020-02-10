## Inverted Half Pyramid

def inverted_half_pyramid(height):
    '''
    Prints pattern for an inverted half pyramid

    Arguments:
    height -- height of the pyramid

    Returns:
    <None>
    '''
    for i in range(height, 0, -1):
        for j in range(1, i+1):
            print('*', end='')
        print()

inverted_half_pyramid(10)