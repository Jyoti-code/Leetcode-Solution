# https://leetcode.com/problems/second-largest-digit-in-a-string/description/

class Solution:
    def secondHighest(self, s: str) -> int:
        x=[]
        for i in s:
            if i.isdigit():
                x.append(i)
        x=set(x)
        a=sorted([int(i) for i in x])
        if len(a)>=2:
            return a[-2]
        else:
            return -1