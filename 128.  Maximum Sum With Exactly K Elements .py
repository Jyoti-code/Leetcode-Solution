# https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        c=max(nums)
        for i in range(k-1):
            a=max(nums)+1
            nums=nums+[a]
            c+=a
        return c