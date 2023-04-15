# https://leetcode.com/problems/binary-prefix-divisible-by-5/description/

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        s=[]
        a=''
        for i in range(len(nums)):
            a+=str(nums[i])
            if int(a,2)%5==0:
                s.append(True)
            else:
                s.append(False)
        return s