class Solution:
    def reverse(self, x: int) -> int:
        rev_num = 0
        c = 0

        if x < 0:
            x *= -1
            c = 1

        while x != 0:
            rem = x % 10
            rev_num = rem + (10 * rev_num)
            x = x // 10

        if c == 1:
            rev_num *= -1

        if rev_num < 2147483648 and rev_num >= -2147483648:
            return rev_num
        else:
            return 0
