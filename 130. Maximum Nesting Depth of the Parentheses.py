# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

class Solution:
    def maxDepth(self, s: str) -> int:
        r=c=0
        for i in range(len(s)):
            if s[i]=='(':
                c+=1
                r=max(r,c)
            elif s[i]==')':
                c-=1
        return r