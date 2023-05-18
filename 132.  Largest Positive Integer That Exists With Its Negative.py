# https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/description/

class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s=set(nums)
        nums=sorted(nums)[::-1]
        for i in nums:
            if 0-i in s:
                return i
        return -1