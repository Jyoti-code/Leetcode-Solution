# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #Pass all test cases
        res=0
        curr=0
        for i,v in enumerate(s):
            if i>=k:
                if s[i-k] in "aeiou":
                    curr-=1
            if s[i] in "aeiou":
                curr+=1
            res=max(res,curr)
        return res

        #TLE pass 99 test cases 
         x=[]
         d="aeiou"
         for i in range(0,len(s)):
             c=0
             for j in range(len(s[i:i+k])):
                 if s[i:i+k][j] in d:
                     c+=1
             x.append(c)
         return max(x)