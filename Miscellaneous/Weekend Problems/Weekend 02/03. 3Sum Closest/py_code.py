import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        closest_sum = sys.maxsize
        
        for i in range(len(nums) - 2):
            ptr_1 = i + 1
            ptr_2 = len(nums) - 1
            
            while ptr_1 < ptr_2:
                summ = nums[i] + nums[ptr_1] + nums[ptr_2]
                
                if abs(target - summ) < abs(target - closest_sum):
                    closest_sum = summ
                
                if summ > target:
                    ptr_2 -= 1
                
                else:
                    ptr_1 += 1
        
        return closest_sum
