# https://leetcode.com/problems/beautiful-array/description/

class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        n1=[1]
        while len(n1)<n:
            e=[2*i for i in n1]
            o=[2*i-1 for i in n1]
            n1=e+o
        return [i for i in n1 if i<=n]        