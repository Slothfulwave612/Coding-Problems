class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_map = {}
        
        for num in nums:
            if hash_map.get(num) != None:
                hash_map[num] += 1
            else:
                hash_map[num] = 1
        
        for key in hash_map:
            if hash_map[key] == 1:
                return key
  
