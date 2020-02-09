## Plus One

def plusOne(digits):
    '''
    The functin will add 1 to last number of the array and do the required computation

    Arguments:
    digits -- an array of digits

    Returns:
    digits -- required array after the summation operation
    '''
    length = len(digits)

    digits[length - 1] = digits[length - 1] + 1
    carry = digits[length - 1] // 10
    digits[length - 1] = digits[length - 1] % 10 

    for i in range(length-2, -1, -1):
        digits[i] = digits[i] + carry
        carry = digits[i] // 10
        digits[i] = digits[i] % 10
    
    if carry == 1:
        digits.insert(0,1)

    return digits

digits1 = [1, 2, 4]
digits2 = [9, 9, 9]

print(plusOne(digits1))
print(plusOne(digits2))