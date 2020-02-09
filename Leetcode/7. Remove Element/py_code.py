## Remove element

def removeElement(nums, val):
    '''
    The function remove the specified value from the array

    Arguments:
    nums -- array of integers
    val -- required value to be deleted
    '''
    i, k = 0, 0
    length = len(nums)

    while k < length:
        if nums[i] == val:
            del nums[i]
        else:
            i += 1
        k += 1
    
    return nums

nums1, val1 = [3, 2, 2, 3], 3
nums2, val2 = [0, 1, 2, 2, 3, 0, 4, 2], 2

print(removeElement(nums1, val1))
print(removeElement(nums2, val2))
