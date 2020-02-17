## Arithematic Series

def is_arithematic(nums):
    '''
    The function returns True if the series of numbers are in arithematic progression
    otherwise False.

    Arguments:
    nums -- a list of integers.

    Returns:
    <bool> -- True if in arithematic progression else False.
    '''

    diff = nums[1] - nums[0]

    for i in range(2, len(nums)):
        diff_2 = nums[i] - nums[i-1]

        if diff_2 != diff:
            return False
    
    return True

nums = [3, -2, -7, -12]
print(is_arithematic(nums))