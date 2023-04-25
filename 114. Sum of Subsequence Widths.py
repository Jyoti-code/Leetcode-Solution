# https://leetcode.com/problems/sum-of-subsequence-widths/description/

class Solution:
    def sumSubseqWidths(self, nums: List[int]) -> int:
        kMod = 10**9+7
        n = len(nums)
        ans = 0
        exp = 1
        nums.sort()
        for i in range(n):
            ans += (nums[i] - nums[n - i - 1]) * exp
            ans %= kMod
            exp = exp * 2 % kMod
        return ans

    # pass only 19 test cases occer TLE problem
    #     result = [[]]
    #     for i in nums:
    #         n = len(result)
    #         for j in range(n):
    #             r = result[j] + [i]
    #             result.append(r)        
    #     s=[]
    #     for i in result[1:]:
    #         a=max(i)
    #         b=min(i)
    #         s.append(a-b)
    #     return sum(s)