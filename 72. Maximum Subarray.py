# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum=-inf
        currsum=0
        for i in nums:
            currsum=max(i,currsum+i)
            maxsum=max(currsum,maxsum)
        return maxsum
