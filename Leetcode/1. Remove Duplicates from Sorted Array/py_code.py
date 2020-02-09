## Remove Duplicate from Sorted Array

def removeDuplicate(nums):
    '''
    The function will return the length of the non-duplicate array.

    Arguments:
    nums -- a list of duplicate numbers

    Returns:
    lens -- length of non-duplicate array
    '''
    
    lens = 1    
    ## initial length is 1 as we will start from second position

    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            nums[lens] = nums[i]
            lens += 1
    
    return lens

nums = [1,1,2,3,4,4,5,6,6]
## the duplicate list

lens = removeDuplicate(nums)
## calling the function

for i in range(lens):
    print(nums[i], end=' ')
## printing non-duplicate array