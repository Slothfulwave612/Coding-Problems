class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        rev = len(s) - 1
        for i in range(len(s) // 2):
            s[i], s[rev] = s[rev], s[i]
            rev -= 1
        
