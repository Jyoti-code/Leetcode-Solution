# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        d=nums[0]
        b=nums[0]
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                d+=nums[i+1]
                b=max(b,d)
            else:
                b=max(b,d)
                d=nums[i+1]
        return max(b,d)
        
