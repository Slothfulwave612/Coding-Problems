class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            temp = i
            
            for j in range(i, len(nums)):
                if nums[temp] >= nums[j]:
                    temp = j
            
            nums[i], nums[temp] = nums[temp], nums[i]
        
