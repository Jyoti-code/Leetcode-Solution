# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/description/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        x=sorted(nums)
        while l<len(nums):
            if x[l]!=nums[l]:
                break
            l+=1
        while r>l:
            if x[r]!=nums[r]:
                break
            r-=1
        return r-l+1