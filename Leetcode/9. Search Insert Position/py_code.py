## Search Insert Position

def searchInsert(nums, target):
    i, j = 0, len(nums) - 1

    while i <= j:
        mid = (i + j) // 2

        if target < nums[mid]:
            j = mid - 1
        
        elif target > nums[mid]:
            i = mid + 1
        
        else:
            return mid
    
    return i

print(searchInsert([1, 3, 5, 6], 5))
print(searchInsert([1, 3, 5, 6], 2))
