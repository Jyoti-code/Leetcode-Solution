# https://leetcode.com/problems/prime-in-diagonal/description/

class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        s=[]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if i==j:
                    s.append(nums[i][j])
                    s.append(nums[i][len(nums)-1-i])        
        a=0
        for i in range(len(s)):
            for j in range(2,int(sqrt(s[i]))+1):
                if s[i]%j==0:
                    break
            else:
                if s[i]>a:
                    a=s[i]
        if a==1:
            return 0
        else:
            return a