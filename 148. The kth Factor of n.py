# https://leetcode.com/problems/the-kth-factor-of-n/description/

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        a=[]
        for i in range(1,n+1):
            if n%i==0:
                a.append(i)
        print(a)
        if len(a)>=k:
            return a[k-1]
        else:
            return -1