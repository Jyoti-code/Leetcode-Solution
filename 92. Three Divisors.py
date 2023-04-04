# https://leetcode.com/problems/three-divisors/description/

class Solution:
    def isThree(self, n: int) -> bool:
        s=[]
        for i in range(1,n+1):
            if n%i==0:
                s.append(i)
        if len(s)==3:
            return True
        else:
            return False