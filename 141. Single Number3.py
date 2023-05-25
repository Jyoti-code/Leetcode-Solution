# https://leetcode.com/problems/single-number-iii/description/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=[]
        x=Counter(nums)
        for i in x:
            if x[i]==1:
                if len(a)!=2:
                    a.append(i)
                else:
                    break
        return a