# https://leetcode.com/problems/left-and-right-sum-differences/description/
class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        pre = 0 
        suf = sum(nums)
        ans = []
        for i in nums: 
            pre += i
            ans.append(abs(pre - suf))
            suf -= i
        return ans