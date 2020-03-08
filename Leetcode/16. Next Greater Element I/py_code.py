class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            flag = False
            for k in range(j+1, len(nums2)):
                if nums2[k] > nums2[j]:
                    output.append(nums2[k])
                    flag = True
                    break
            if flag == False:
                output.append(-1)
        
        return output
