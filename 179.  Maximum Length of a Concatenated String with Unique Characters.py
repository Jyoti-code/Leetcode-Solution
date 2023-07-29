# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/description/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        res=[""]
        c=0
        for i in arr:
            for j in res:
                new=j+i
                if len(new)!=len(set(new)):
                    continue
                res.append(new)
                c=max(c,len(new))
        return c