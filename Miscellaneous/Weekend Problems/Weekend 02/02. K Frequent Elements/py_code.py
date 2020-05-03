class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        
        for i in nums:
            if hash_map.get(i) == None:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        
        j = 0
        a = [0] * len(hash_map)
        
        for i in hash_map:
            a[j] = [i, hash_map[i]]
            j += 1
        
        a = sorted(a, key= lambda x: x[1], reverse=True)
        
        output_list = []
        
        for i in range(k):
            output_list.append(a[i][0])
        
        return output_list
        
