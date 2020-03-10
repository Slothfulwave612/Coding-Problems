class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = []
        length_inp = len(nums)
        
        inp_index = 0
        
        while inp_index != length_inp:
            trav_index = (inp_index + 1) % length_inp
            
            while trav_index != inp_index:
                if nums[trav_index] > nums[inp_index]:
                    output.append(nums[trav_index])
                    break
                trav_index = (trav_index + 1) % length_inp
            else:
                output.append(-1)
                
            inp_index += 1
        
        return output
