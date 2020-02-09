## Array Partition I

def arrayPartition(nums):
    '''
    The function will sum up the required numbers.

    Arguments:
    nums -- an array of integers

    Returns:
    <int> -- an int value which is the required sum
    '''

    nums.sort()
    return sum(nums[::2])

nums = [1, 4, 3, 2]

print(arrayPartition(nums))