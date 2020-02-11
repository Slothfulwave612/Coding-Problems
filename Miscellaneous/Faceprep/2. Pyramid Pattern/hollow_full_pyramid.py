## Hollow Full Pyramid

def hollow_full_pyramid(height):
    '''
    Prints the pattern for hollow full pyramid

    Arguments:
    height -- height of the pyramid

    Returns:
    <None>
    '''
    for i in range(1, height + 1):
        for j in range(i, height):
            print(' ', end='')
        for k in range(1, i + 1):
            if i == 1 or i == height:
                print('*', end=' ')
            else:
                if k == 1 or k == i:
                    print('*', end=' ')
                else:
                    print(end='  ')
        print()

hollow_full_pyramid(10)