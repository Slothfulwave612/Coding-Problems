import math
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        sqrt_num = int(math.sqrt(num))
        
        if sqrt_num * sqrt_num == num:
            return True
        else:
            return False
