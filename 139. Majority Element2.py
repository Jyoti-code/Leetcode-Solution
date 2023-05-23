# https://leetcode.com/problems/majority-element-ii/description/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        x=Counter(nums)
        a=[]
        for i in x:
            if x[i]>len(nums)//3:
                a.append(i)
        return a