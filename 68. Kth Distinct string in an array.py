# https://leetcode.com/problems/kth-distinct-string-in-an-array/description/

from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        x=Counter(arr)
        a=[]
        for i in x:
            if x[i]==1:
                a.append(i)
        for i in range(k):
            if len(a)>=k:
                return a[k-1]
        return ""