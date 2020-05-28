'''
Happy and Unhappy Number.

Happy number: Starting with any positive integer, replace the number by the sum of the 
squares of its digits, and repeat the process until the number equals 1(where it will stay),
or it loops endlessly in a cycle which does not include 1.
'''

def happy_number(num):
    '''
    Function to check whether a number is happy or unhappy.

    Argument:
    num -- int, number to be checked.

    Returns:
    str, 'Happy' or 'Unhappy'.
    '''

    while num != 1 and num != 4: 
        num = [int(x) for x in str(num)]

        num = sum(map(lambda i: i*i, num))

    if num == 1:
        print('Happy Number')
    else:
        print('Unhappy Number')

num_1 = 19
happy_number(num_1)

num_2 = 14
happy_number(num_2)

num_3 = 27
happy_number(num_3)
