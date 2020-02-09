## Move Zeroes

def moveZeroes(nums):
    '''
    This function moves the zeroes to the end of the array

    Arguments:
    nums -- an array of integers

    Returns:
    <list> -- resultant array having zeroes at end
    '''

    pos = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[pos] = nums[pos], nums[i]
            pos += 1
    
    return nums

nums = [1, 0, 0, 3, 0, 12]

print(moveZeroes(nums))