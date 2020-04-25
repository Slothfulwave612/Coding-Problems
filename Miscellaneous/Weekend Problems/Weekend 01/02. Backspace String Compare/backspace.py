class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        i = len(S)
        j = len(T)
        
        while i >= 0  and j >= 0:
            backspace = 0
            
            while backspace >= 0:
                i -= 1
                
                if i >= 0 and S[i] == '#':
                    backspace += 1
                else:
                    backspace -= 1
            
            backspace = 0
            
            while backspace >= 0:
                j -= 1
                
                if j >= 0 and T[j] == '#':
                    backspace += 1
                else:
                    backspace -= 1
            
            if i >= 0 and j >= 0 and S[i] != T[j]:
                return False
        
        return i < 0 and j < 0
