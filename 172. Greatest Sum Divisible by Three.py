# https://leetcode.com/problems/greatest-sum-divisible-by-three/description/

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp=[0]*3
        for i in nums:
            a,b,c=dp[0]+i,dp[1]+i,dp[2]+i
            dp[a%3]=max(dp[a%3],a)
            dp[b%3]=max(dp[b%3],b)
            dp[c%3]=max(dp[c%3],c)
        return dp[0]