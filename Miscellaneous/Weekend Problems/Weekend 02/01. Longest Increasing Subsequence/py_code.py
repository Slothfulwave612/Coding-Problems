class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        length = len(nums)
        
        lis = [1] * length
        
        for i in range(1, length):
            for j in range(0, i):
                if nums[i] > nums[j] and lis[i] < lis[j] + 1:
                    lis[i] = lis[j] + 1
        
        return max(lis)
    
