## Half Pyramid

def half_pyramid(height):
    '''
    Print a pattern for half pyramid

    Arguments:
    height -- the height of the pyramid

    Returns:
    <None>
    '''
    for i in range(height):
        for j in range(i+1):
            print('*', end='')
        print()

half_pyramid(6)