def compute_result(a, b):
    if len(a) >= len(b):
        return sum_list(a, b)
    else:
        return sum_list(b, a)

def sum_list(a, b):
    '''
    Function to add two list.

    Arguments:
    a -- list, representing our first number.
    b -- list, representing our second number.

    Returns:
    c -- list, representing the sum of a and b
    '''
    len_a, len_b = len(a), len(b)       ## length of a and b

    max_length = max(len_a, len_b)      ## maximum length, on comparing length of both lists

    c = [0] * (max_length + 1)               ## making a third list which will store the sum of first two
                                             ## +1 because we need size of output array to be 1 more than the maximum size list

    i, j = len(a) - 1, len(b) - 1     ## i for first list and j for second
    carry = 0                         ## initial carry is zero

    while i >= 0 and j >= 0:
        s = a[i] + b[j] + carry

        carry = s // 10               ## carry = s / 10

        c[i+1] = s % 10

        i -= 1
        j -= 1
    
    while i >= 0:
        s = a[i] + carry
        carry = s // 10

        c[i+1] = s % 10
        i -= 1
    
    if carry != 0:
        c[0] = carry

    return c

## first case
a1 = [3, 5, 2]     ## first number
b1 = [1, 2, 1]     ## second number

## second case
a2 = [7, 8, 9]     ## first number
b2 = [9, 8, 7]     ## second number

## third case
a3 = [1, 0, 4, 8]     ## first number
b3 = [1, 5, 1]        ## second number

## fourth case
a4 = [9, 9, 9, 9, 9, 9]
b4 = [9, 9]

## fifth case
a5 = [9, 9]
b5 = [9, 9, 9, 9, 9, 9]

sum_result_1 = compute_result(a1, b1)     ## first case
print(sum_result_1)

sum_result_2 = compute_result(a2, b2)     ## second case
print(sum_result_2)

sum_result_3 = compute_result(a3, b3)     ## third case
print(sum_result_3)

sum_result_4 = compute_result(a4, b4)     ## fourth case
print(sum_result_4)

sum_result_5 = compute_result(a5, b5)     ## fifth case
print(sum_result_5)
