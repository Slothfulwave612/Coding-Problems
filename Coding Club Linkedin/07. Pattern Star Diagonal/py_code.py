## Pattern Star Diagonal
## Time complexity O(n2)

def pattern_star_diagonal(n):
    '''
    Prints the required pattern.

    Arguments:
    n -- integer value

    Returns:
    <None>
    '''

    for i in range(1, n+1):
        for j in range(n, 0, -1):
            if j == i:
                print('*', end='')
            else:
                print(j, end='')
        print()

n = 8
pattern_star_diagonal(n)
            