# https://leetcode.com/problems/count-nice-pairs-in-an-array/description/

class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        c=0
        d={}
        for i in nums:
            a=i-int(str(i)[::-1])
            if a not in d:
                d[a]=1
            else:
                d[a]+=1
        for i in d.values():
            c+=(i*(i-1)//2)
        return c%(10**9+7)