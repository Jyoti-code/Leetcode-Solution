# https://leetcode.com/problems/count-subarrays-with-fixed-bounds/description/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        '''c=0
        s=[]
        for i in range(len(nums)+1):
            for j in range(i):
                s.append(nums[j:i])
        for i in range(len(s)):
            if max(s[i])<=maxK and min(s[i])<=minK:
                if maxK in s[i] and minK in s[i]:
                    c+=1
        return c'''
        '''res=0
        for i in range(len(nums)):
            min1=max1=nums[i]
            for j in range(i,len(nums)):
                min1=min(min1,nums[j])
                max1=max(max1,nums[j])
                if min1<minK or max1>maxK:
                    break
                if min1==minK and max1==maxK:
                    res+=1
        return res'''

        minfound = maxfound = False
        start = minstart = maxstart = 0
        total = 0

        for i in range(len(nums)):
            if nums[i] == minK:
                minstart = i
                minfound = True
            if nums[i] == maxK:
                maxstart = i
                maxfound = True
            if not minK <= nums[i] <= maxK:
                minfound = maxfound = False
                start = i+1
            if minfound and maxfound:
                total += min(minstart,maxstart) - start + 1

        return total

