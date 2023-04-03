# https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/description/

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n+1):
            a=i
            b=n-i
            if str(a).count('0')>=1 or str(b).count('0')>=1:
                continue
            elif a+b==n:
                return [a,b]
            
            