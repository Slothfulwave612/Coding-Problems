class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        min_length = len(min(strs))
        
        i, j, prefix = 0, 0, ''
        
        while j < min_length:
            
            if i == len(strs) - 1:
                prefix += strs[i][j]
                i = 0
                j += 1
            
            elif strs[i][j] == strs[i+1][j]:
                i += 1
                
            else:
                return prefix
        
        return prefix
