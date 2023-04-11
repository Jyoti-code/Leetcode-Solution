# https://leetcode.com/problems/average-value-of-even-numbers-that-are-divisible-by-three/description/

class Solution:
    def averageValue(self, nums: List[int]) -> int:
        s=[]
        for i in range(len(nums)):
            if nums[i]%2==0 and nums[i]%3==0:
                s.append(nums[i])
        if len(s)>0:
            return sum(s)//len(s)
        else:
            return 0