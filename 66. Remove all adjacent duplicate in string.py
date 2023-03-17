# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

class Solution:
    def removeDuplicates(self, s: str) -> str:
        x=[]
        for i in s:
            if x and x[-1]==i:
                x.pop()
            else:
                x.append(i)
        return "".join(x)