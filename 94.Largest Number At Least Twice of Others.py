# https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        s=sorted(nums)
        if s[-1]>=2*s[-2]:
            return nums.index(s[-1])
        return -1
        