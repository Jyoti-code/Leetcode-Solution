# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        currsum=0
        minwin=len(nums)+1
        for i in range(len(nums)):
            currsum+=nums[i]
            if currsum>=target:
                while currsum>=target:
                    minwin=min(minwin,i-s+1)
                    currsum-=nums[s]
                    s+=1
        if minwin==len(nums)+1:
            return 0
        else:
            return minwin
        # s=[]
        # for i in range(len(nums)=1):
        #     if nums[i]==target or nums[i+1]==target:
        #         return 1
        #     if nums[i]+nums[i+1]==target:
        #         s.append(nums[i])
        #         s.append(nums[i+1])
        # return len(s)