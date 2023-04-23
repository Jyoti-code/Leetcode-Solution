# https://leetcode.com/problems/permutations-ii/description/

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        a=permutations(nums,len(nums))
        x=[]
        for i in list(a):
            x.append(i)
        x=set(x)
        return list(x)