## Happy Number

def square_digit_sum(num):
    '''
    Function calculates sum of square of digits.

    Arguments:
    num -- integer value

    Output:
    summ -- sum of square of digits
    '''

    summ = 0

    while num != 0:
        rem = num % 10
        summ += (rem * rem)
        num = num // 10

    return summ

def is_happy(num):
    '''
    Function returns True if number is happy otherwise False

    Arguments:
    num -- integer value

    Output:
    str -- 'Happy Number' or 'Unhappy Number'
    '''
    
    slow = fast = num

    while True:
        slow = square_digit_sum(slow)

        fast = square_digit_sum(square_digit_sum(fast))

        if slow != fast:
            continue
        else:
            break
    
    if slow == 1:
        return 'Happy Number'
    else:
        return 'Unhappy Number'

num1 = 82
num2 = 13
num3 = 161

result1 = is_happy(num1)
result2 = is_happy(num2)
result3 = is_happy(num3)

print(f'{num1} is {result1}')
print(f'{num2} is {result2}')
print(f'{num3} is {result3}')