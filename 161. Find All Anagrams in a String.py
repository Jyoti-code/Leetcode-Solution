# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        a=len(s)
        b=len(p)
        if a<b:
            return
        x=[]
        p=Counter(p)
        for i in range(a-b+1):
            if Counter(s[i:i+b])==p:
                x.append(i)
        return x

        # pass only 34 test cases TLE occur

        # a=[s[i:i+len(p)] for i in range(len(s))]
        # x=[]
        # for i in range(len(a)):
        #     if sorted(a[i])==sorted(p):
        #         x.append(i)
        # return x