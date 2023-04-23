# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/description/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if sorted(target)==sorted(arr):
            return True
        else:
            return False