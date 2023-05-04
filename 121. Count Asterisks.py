# https://leetcode.com/problems/count-asterisks/description/

class Solution:
    def countAsterisks(self, s: str) -> int:
        s=s.split('|')
        x=[]
        for i in range(0,len(s)):
            x.append(s[i].count('*'))
        return sum(x[::2])