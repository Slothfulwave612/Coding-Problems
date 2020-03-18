class Solution:
    def minSteps(self, n: int) -> int:
        result = 0
        d = 2
        
        while n > 1:
            while n % d == 0:
                result += d
                n = n // d
            d += 1
        
        return result
