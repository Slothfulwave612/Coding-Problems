class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        left, right = 0, len(nums)-1
        
        while left <= right:
            
            mid = (left + right) // 2
            
            if left == right == mid:
                if nums[mid] == target:
                    return mid
                else:
                    return -1
            
            if target == nums[mid]: 
                return mid
            
            elif nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else: 
                    left = mid+1
            
            else: 
                if nums[mid+1] <= target <= nums[right]: 
                    left = mid+1
                else: 
                    right = mid

        return -1
