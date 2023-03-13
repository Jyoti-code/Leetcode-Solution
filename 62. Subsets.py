# https://leetcode.com/problems/subsets/

import math
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s=[]
        n=len(nums)
        for i in range(pow(2,n)):
            a=[nums[j] for j in range(n) if (i & (pow(2,j)))]
            s.append(a)
        return s

       