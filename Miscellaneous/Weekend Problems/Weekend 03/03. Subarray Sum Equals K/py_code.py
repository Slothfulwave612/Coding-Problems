class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dict = {0: 1}
        count = 0
        summ = 0
        
        for num in nums:
            summ += num
            
            if sum_dict.get(summ - k) != None:
                count += sum_dict[summ - k]
            
            if sum_dict.get(summ) == None:
                sum_dict[summ] = 1
            else:
                sum_dict[summ] += 1
        
        return count
        
