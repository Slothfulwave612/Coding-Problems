## Hollow Inverted Half Pyramid

def hollow_inverted_half_pyramid(height):
    '''
    Prints a pattern for inverted half pyramid

    Arguments:
    height -- height of the pyramid

    Returns:
    <None>
    '''
    for i in range(height, 0, -1):
        for j in range(1, i+1):
            if i == height or i == 1:
                print('*', end='')
            else:
                if j == 1 or j == i:
                    print('*', end='')
                else:
                    print(end=' ')
        print()

hollow_inverted_half_pyramid(15)