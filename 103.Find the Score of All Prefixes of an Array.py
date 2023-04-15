class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        s=[nums[0]+nums[0]]
        maxx=nums[0]
        for i in range(1,len(nums)):
            if (maxx<nums[i]):
                maxx=nums[i]
            a=nums[i]+maxx
            s.append(a)
        c=[]
        x=0
        for i in s:
            x+=i
            c.append(x)
        return c