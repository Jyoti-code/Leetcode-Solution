# https://leetcode.com/problems/neither-minimum-nor-maximum/description/

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        s=sorted(nums)
        if len(s)>=3:
            return s[1]
        else:
            return -1