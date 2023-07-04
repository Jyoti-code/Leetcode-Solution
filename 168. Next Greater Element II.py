# https://leetcode.com/problems/next-greater-element-ii/description/

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans=[]
        flag=False
        for i in range(len(nums)):
            j=i+1
            rot=len(nums)-1
            while rot>0:
                if j>=len(nums):
                    j=0
                if nums[i]<nums[j]:
                    ans.append(nums[j])
                    flag=True
                    break
                else:
                    rot-=1
                    j+=1
                    flag=False
            if flag==False:
                ans.append(-1)
        return ans
        # s=[]
        # for i in range(len(nums)):
        #     if nums[i]+1 in nums:
        #         s.append(nums[i]+1)
        #     if nums[i]==max(nums):
        #         s.append(-1)
        # return s