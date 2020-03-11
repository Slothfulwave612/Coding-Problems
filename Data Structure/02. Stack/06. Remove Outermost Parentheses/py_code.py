class Solution:
    def removeOuterParentheses(self, S):
        a = [1 if item == '(' else -1 for item in S ]

        acc_sum = 0
        count = 0
        b = 0
        l = []

        for item in a:
            acc_sum += item
            a[count] = acc_sum
            count += 1

        for i in range(len(a)):
            if a[i] == 0:
                l.append(S[b:i+1])
                b = i + 1
        
        return ''.join(grp[1:-1] for grp in l)    
           
