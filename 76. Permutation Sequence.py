# https://leetcode.com/problems/permutation-sequence/description/

from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        c=[]
        s="".join([str(i) for i in range(1,n+1)])
        x=permutations(s)
        for i in list(x):
            a="".join(i)
            c.append(a)
        return c[k-1]