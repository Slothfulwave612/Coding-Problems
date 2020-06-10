class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = 0
        
        for num in nums:
            if target > num:
                index += 1
            
            if target == num:
                return index
            
            if target < num:
                return index
        
        return index
