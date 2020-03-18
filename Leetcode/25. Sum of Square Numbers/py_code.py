import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(0, int(math.sqrt(c)) + 1):
            b = math.sqrt(c - i*i)
            if b == int(b):
                return True
        return False
