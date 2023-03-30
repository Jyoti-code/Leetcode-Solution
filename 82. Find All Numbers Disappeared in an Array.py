# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # a=max(nums)
        s=[i for i in range(1,len(nums)+1)]
        x=set(s)-set(nums)
        return list(x)