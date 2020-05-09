class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_elem = nums[0]
        max_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_elem = max(nums[i], current_elem + nums[i])
            max_sum = max(current_elem, max_sum)
        
        return max_sum
