# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(nums)-{0})
        