# https://leetcode.com/problems/single-number-ii/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        x=Counter(nums)
        for i in x:
            if x[i]==1:
                return i