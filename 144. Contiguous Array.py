# https://leetcode.com/problems/contiguous-array/description/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        m=0
        c=0
        d={0:-1}
        for i in range(len(nums)):
            if nums[i]==0:
                c-=1
            else:
                c+=1
            if c in d:
                m=max(m,i-d[c])
            else:
                d[c]=i
        return m


   