## Hollow Rectangle

def hollow_rectangle(rows, cols):
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if i == 1 or i == rows:
                print('*', end='')
            else:
                if j == 1 or j == cols:
                    print('*', end='')
                else:
                    print(' ', end='')
        print()

hollow_rectangle(5,7)