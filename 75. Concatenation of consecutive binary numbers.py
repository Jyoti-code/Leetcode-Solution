# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/description/

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s=[]
        for i in range(n+1):
            x=bin(i).replace("0b","")
            s.append(x)
        a="".join(s)
        return int(a,2)%(10**9+7)