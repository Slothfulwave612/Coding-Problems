class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        min_length, length = len(nums) + 1, len(nums)
        start, end = 0, 0
        current_sum = 0
        
        while end < length:
            
            while end < length and current_sum < s:
                current_sum += nums[end]
                end += 1
            
            while start < length and current_sum >= s:
                if end - start < min_length:
                    min_length = end - start
                
                current_sum -= nums[start]
                start += 1
        
        if min_length == len(nums) + 1:
            return 0
        
        return min_length
        
