# https://leetcode.com/problems/k-diff-pairs-in-an-array/description/

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c=Counter(nums)
        if k>0:
            return sum([i+k in c for i in c])
        else:
            return sum([c[i]>1 for i in c])
        # c=0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]-nums[j]==k:
        #             c+=1
        # return c
        