## Excel Column Count

def col_name(col_num):
    '''
    The function returns the name of the column corresponding to the col_num.

    Arguments:
    col_num -- column number, an integer.

    Returns:
    name_col -- a str, which is the column name.
    '''
    
    name_col = ''

    while col_num > 0:
        rem = col_num % 26
        col_num = col_num // 26
    
        if rem == 0:
            name_col += 'Z'
            col_num -= 1
        else:
            name_col += chr(ord('A') + (rem - 1))
    
    return name_col[::-1]

col_num1 = 54
col_num2 = 10
col_num3 = 30
col_num4 = 26
col_num5 = 42

print(f'{col_num1}: {col_name(col_num1)}')
print(f'{col_num2}: {col_name(col_num2)}')
print(f'{col_num3}: {col_name(col_num3)}')
print(f'{col_num4}: {col_name(col_num4)}')
print(f'{col_num5}: {col_name(col_num5)}')