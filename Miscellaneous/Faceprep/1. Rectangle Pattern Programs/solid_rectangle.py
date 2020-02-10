## Solid Rectangle

def solid_rectangle(rows, cols):
    '''
    Prints pattern for solid rectangle

    Arguments:
    rows -- number of rows
    cols -- number of cols

    Returns:
    <none>
    '''
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            print('*', end='')
        print()

solid_rectangle(4,7)