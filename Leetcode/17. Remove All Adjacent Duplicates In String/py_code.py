class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        stack.append(S[0])
        
        for i in range(1, len(S)):
            item = S[i]
            
            if len(stack) == 0:
                stack.append(item)
            else:
                x = stack.pop()
                
                if x != item:
                    stack.append(x)
                    stack.append(item)
        
        return ''.join(elem for elem in stack)
            
            
