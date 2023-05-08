# https://leetcode.com/problems/find-xor-sum-of-all-pairs-bitwise-and/description/

class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        a=0
        for i in arr1:
            a^=i
        b=0
        for j in arr2:
            b^=j
        return a&b


        #Pass 74 test cases TLE
         s=[]
         for i in range(len(arr1)):
             for j in range(len(arr2)):
                 s.append(arr1[i]&arr2[j])
         x=s[0]
         for i in range(1,len(s)):
             x^=s[i]
         return x